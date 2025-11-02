# voting/views_payment.py
from rest_framework import generics
from rest_framework.response import Response
from django.db import transaction
from django.conf import settings
from .models import VoteIntent, Campaign
import uuid
from .payments import campay

class VoteIntentCreate(generics.CreateAPIView):
    """
    Creates our local VoteIntent, then calls CamPay to start a real collect.
    The user will receive a MoMo/OM prompt on their phone.
    """
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            votes_req = int(data.get("votes_requested", 1)); assert votes_req > 0
            candidate_id = int(data["candidate_id"])
            provider = data.get("provider", "").upper() or "MTN"
            phone = str(data["payer_phone"]).strip()
            assert phone and phone.isdigit()
        except Exception:
            return Response({"detail": "Invalid input"}, status=400)

        camp = Campaign.objects.filter(is_active=True).first()
        if not camp:
            return Response({"detail":"No active campaign"}, status=400)

        amount = votes_req * camp.price_per_vote
        payment_ref = uuid.uuid4().hex[:20]
        description = f"Vote {votes_req}x for candidate {candidate_id}"

        with transaction.atomic():
            intent = VoteIntent.objects.create(
                candidate_id=candidate_id, campaign=camp, votes_requested=votes_req,
                amount=amount, payment_ref=payment_ref, provider=provider,
                payer_phone=phone, ip=request.META.get("REMOTE_ADDR"),
                user_agent=request.META.get("HTTP_USER_AGENT","")
            )

        # --- Call CamPay to initiate the collect ---
        try:
            gateway_res = campay.request_collect(
                reference=payment_ref,
                amount=amount,
                currency=camp.currency or "XAF",
                payer_phone=phone,
                provider=provider,
                description=description
            )
        except campay.CampayError as e:
            # mark local intent as failed to start
            with transaction.atomic():
                intent.status = "FAILED"
                intent.save(update_fields=["status"])
            return Response({"detail":"Payment init failed", "error": str(e)}, status=502)

        # You can inspect gateway_res to show additional info in UI
        return Response({
            "intent_id": intent.id,
            "amount": amount,
            "payment_ref": payment_ref,
            "status": intent.status,
            "gateway": gateway_res,
            "checkout_info": {"message": "Payment prompt sent. Approve on your phone."}
        }, status=201)
