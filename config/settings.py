"""
Django settings for a STATIC portfolio site (built to plain HTML for GitHub Pages).
Django is used as a templating + build engine; there is no database or server at runtime.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "build-only-not-secret")
DEBUG = os.environ.get("DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "portfolio",
]
MIDDLEWARE = []
ROOT_URLCONF = "config.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "portfolio.context.site",
    ]},
}]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
USE_TZ = True
TIME_ZONE = "Asia/Kolkata"
LANGUAGE_CODE = "en"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---- Static files ---------------------------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ---- Site configuration (edit these, or set as env vars / GitHub repo variables)
SITE = {
    # Full public URL with NO trailing slash, e.g. "https://adityaaryan.me" or
    # "https://<username>.github.io/<repo>". Used for canonical URLs, sitemap, RSS, OG tags.
    "url": os.environ.get("SITE_URL", "https://aditya-aryan-6914.github.io").rstrip("/"),
    # Leave "" for a custom domain / user site (<username>.github.io).
    # For a project site at https://<user>.github.io/<repo>/ set to "/<repo>".
    "base_path": os.environ.get("BASE_PATH", "").rstrip("/"),
    "name": "Aditya Aryan",
    "series_name": "THE SERIES",
    "adsense_client": os.environ.get("ADSENSE_CLIENT", ""),      # e.g. ca-pub-1234567890123456
    "adsense_slot": os.environ.get("ADSENSE_SLOT", ""),            # optional in-article ad unit id (Auto ads work without it)
    "ga_id": os.environ.get("GA_ID", ""),                          # e.g. G-XXXXXXXXXX
    "search_console_token": os.environ.get("GSC_TOKEN", ""),       # google-site-verification value
    # Contact form backend: create a free form at formspree.io and paste the endpoint.
    "formspree_endpoint": os.environ.get("FORMSPREE_ENDPOINT", ""),
    "custom_domain": os.environ.get("CUSTOM_DOMAIN", ""),  # written to CNAME ("" to skip)
}
