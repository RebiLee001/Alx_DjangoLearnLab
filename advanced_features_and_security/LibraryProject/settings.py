INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'relationship_app',
    'accounts',
]
AUTH_USER_MODEL = "bookshelf.CustomUser"

# ==========================
# SECURITY SETTINGS
# ==========================

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Proxy SSL header support
SECURE_PROXY_SSL_HEADER = ("SECURE_PROXY_SSL_HEADER", "HTTP_X_FORWARDED_PROTO")