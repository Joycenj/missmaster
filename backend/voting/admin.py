from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Campaign, Candidate, VoteIntent, Vote

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("display_name", "category", "votes_count", "is_active", "preview")
    search_fields = ("display_name",)
    list_filter = ("category", "is_active")
    readonly_fields = ("preview", "slug")
    fieldsets = (
        (None, {
            "fields": ("display_name","slug","category","is_active")
        }),
        ("Descriptions", {
            "fields": ("short_description","bio")
        }),
        ("Photo", {
            "fields": ("photo","photo_url","preview")
        }),
        ("Stats", {
            "fields": ("votes_count",),
        }),
    )
    def preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height:120px;border-radius:8px;" />', obj.photo.url)
        if obj.photo_url:
            return format_html('<img src="{}" style="max-height:120px;border-radius:8px;" />', obj.photo_url)
        return "-"
    preview.short_description = "Preview"

admin.site.register([Category, Campaign, VoteIntent, Vote])
