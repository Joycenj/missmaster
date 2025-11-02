from rest_framework import serializers
from .models import Category, Candidate, VoteIntent


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CandidateListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    photo_src = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = (
            "id",
            "slug",
            "display_name",
            "short_description",
            "photo_src",
            "category",
            "votes_count",
        )

    def get_photo_src(self, obj):
        # Prefer uploaded image; else use photo_url
        url = obj.photo.url if obj.photo else obj.photo_url
        if not url:
            return None
        request = self.context.get("request")
        # Make it absolute so the frontend can load it from localhost:8000
        return request.build_absolute_uri(url) if request else url


class CandidateDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    photo_src = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = (
            "id",
            "slug",
            "display_name",
            "short_description",
            "bio",
            "photo_src",
            "category",
            "votes_count",
        )

    def get_photo_src(self, obj):
        url = obj.photo.url if obj.photo else obj.photo_url
        if not url:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(url) if request else url


class VoteIntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteIntent
        fields = ("id", "payment_ref", "status", "amount")
