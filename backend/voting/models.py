from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=120)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    price_per_vote = models.PositiveIntegerField(default=100)  # FCFA
    currency = models.CharField(max_length=5, default="XAF")

def candidate_upload_path(instance, filename):
    return f"candidates/{instance.slug or 'candidate'}/{filename}"

class Candidate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    display_name = models.CharField(max_length=120)
    short_description = models.CharField(max_length=200, blank=True)  # NEW
    bio = models.TextField(blank=True)
    # Prefer ImageField for admin upload
    photo = models.ImageField(upload_to=candidate_upload_path, blank=True)  # NEW
    photo_url = models.URLField(blank=True)  # optional fallback (remote URL)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    votes_count = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.display_name)
        return super().save(*args, **kwargs)
    def __str__(self): return self.display_name

class VoteIntent(models.Model):
    PROVIDERS = (("MTN","MTN"),("ORANGE","ORANGE"))
    STATUSES = (("PENDING","PENDING"),("PAID","PAID"),("FAILED","FAILED"),("EXPIRED","EXPIRED"))
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    campaign  = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    votes_requested = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    payment_ref = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=10, choices=STATUSES, default="PENDING")
    payer_phone = models.CharField(max_length=20)
    provider = models.CharField(max_length=10, choices=PROVIDERS)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    vote_intent = models.OneToOneField(VoteIntent, on_delete=models.PROTECT)
    candidate   = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    campaign    = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    votes       = models.PositiveIntegerField(default=1)
    created_at  = models.DateTimeField(auto_now_add=True)
