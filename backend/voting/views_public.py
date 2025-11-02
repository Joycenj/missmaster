from rest_framework import generics
from .models import Category, Candidate, VoteIntent
from .serializers import CategorySerializer, CandidateListSerializer, CandidateDetailSerializer, VoteIntentSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

class CandidateList(generics.ListAPIView):
    serializer_class = CandidateListSerializer
    def get_queryset(self):
        qs = Candidate.objects.filter(is_active=True, category__is_active=True).select_related("category")
        cat = self.request.query_params.get("category")
        if cat:
            qs = qs.filter(category__name__iexact=cat)
        q = self.request.query_params.get("search")
        if q:
            qs = qs.filter(display_name__icontains=q)
        return qs

class CandidateDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Candidate.objects.filter(is_active=True).select_related("category")
    serializer_class = CandidateDetailSerializer

class VoteIntentDetail(generics.RetrieveAPIView):
    queryset = VoteIntent.objects.all()
    serializer_class = VoteIntentSerializer
