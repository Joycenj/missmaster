from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# --------------------------------------------------
# BASIC CONFIG
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

TIME_ZONE = "Africa/Douala"
USE_TZ = True
LANGUAGE_CODE = "en-us"

# --------------------------------------------------
# INSTALLED APPS
# --------------------------------------------------
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "corsheaders",

    # Local apps
    "voting",
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",       # static files (Render)
    "corsheaders.middleware.CorsMiddleware",            # must be high
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "voting_api.urls"
WSGI_APPLICATION = "voting_api.wsgi.application"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------
# Default SQLite (local)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Optional: switch automatically if DATABASE_URL is set (Render/Railway)
DB_URL = os.getenv("DATABASE_URL")
if DB_URL:
    import dj_database_url
    DATABASES["default"] = dj_database_url.parse(DB_URL, conn_max_age=600)

# --------------------------------------------------
# AUTH / PASSWORD VALIDATORS
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# STATIC & MEDIA (WhiteNoise)
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# REST FRAMEWORK
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# --------------------------------------------------
# CORS / CSRF
# --------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",                    # Local dev
    # add prod URLs after deployment:
    # "https://missmaster-frontend.vercel.app",
    # "https://www.missmasterudm.com",
]
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if os.getenv("CSRF_TRUSTED_ORIGINS") else []

# --------------------------------------------------
# CAMPAY ENV CONFIG (read by your views)
# --------------------------------------------------
CAMPAY_ENABLE = os.getenv("CAMPAY_ENABLE", "false").lower() == "true"
CAMPAY_MODE = os.getenv("CAMPAY_MODE", "test")
CAMPAY_BASE_URL = os.getenv("CAMPAY_BASE_URL", "https://api.campay.co")
CAMPAY_CLIENT_ID = os.getenv("CAMPAY_CLIENT_ID", "")
CAMPAY_CLIENT_SECRET = os.getenv("CAMPAY_CLIENT_SECRET", "")
CAMPAY_WEBHOOK_URL = os.getenv("CAMPAY_WEBHOOK_URL", "")

# --------------------------------------------------
# DEFAULT AUTO FIELD
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
