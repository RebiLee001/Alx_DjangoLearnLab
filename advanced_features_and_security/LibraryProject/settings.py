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

# -------------------------------
# SECURITY CONFIGURATIONS
# -------------------------------

# Browser-side protections
SECURE_BROWSER_XSS_FILTER = True            # Enable XSS filter in browser
SECURE_CONTENT_TYPE_NOSNIFF = True          # Prevent MIME-type sniffing
X_FRAME_OPTIONS = 'DENY'                    # Prevent clickjacking

# Cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
