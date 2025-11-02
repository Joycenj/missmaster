from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

from voting.views_public import CategoryList, CandidateList, CandidateDetail, VoteIntentDetail
from voting.views_payment import VoteIntentCreate
from voting.views_webhook import campay_webhook

def health(_): return JsonResponse({"ok": True})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/categories/", CategoryList.as_view()),
    path("api/candidates/", CandidateList.as_view()),
    path("api/candidates/<slug:slug>/", CandidateDetail.as_view()),
    path("api/vote-intents/", VoteIntentCreate.as_view()),
    path("api/vote-intents/<int:pk>/", VoteIntentDetail.as_view()),
    path("api/payments/campay/webhook/", campay_webhook),
    path("health/", health)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
