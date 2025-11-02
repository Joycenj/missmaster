from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction
from django.db.models import F
from .models import VoteIntent, Vote, Candidate
from .payments.verify import valid_signature

@api_view(["POST"])
@permission_classes([AllowAny])
@transaction.atomic
def campay_webhook(request):
    if not valid_signature(request.body, request.headers.get("X-Campay-Signature","")):
        return Response(status=403)
    payload = request.data
    ref = payload.get("reference")
    status_code = payload.get("status")
    try:
        intent = VoteIntent.objects.select_for_update().get(payment_ref=ref)
    except VoteIntent.DoesNotExist:
        return Response(status=404)
    if intent.status == "PAID":
        return Response({"ok": True})
    if status_code == "SUCCESS":
        intent.status = "PAID"
        intent.save(update_fields=["status"])
        Vote.objects.create(
            vote_intent=intent, candidate=intent.candidate, campaign=intent.campaign, votes=intent.votes_requested
        )
        Candidate.objects.filter(pk=intent.candidate_id).update(
            votes_count=F("votes_count")+intent.votes_requested
        )
    else:
        intent.status = "FAILED"
        intent.save(update_fields=["status"])
    return Response({"ok": True})
