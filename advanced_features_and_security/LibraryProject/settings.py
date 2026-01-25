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

# SECURITY CONFIGURATION

# 1. Turn off DEBUG in production
DEBUG = False

# 2. Browser security settings
SECURE_BROWSER_XSS_FILTER = True      # Enables XSS filter in the browser
SECURE_CONTENT_TYPE_NOSNIFF = True    # Prevents the browser from MIME-sniffing
X_FRAME_OPTIONS = 'DENY'              # Prevent clickjacking

# 3. Cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# 4. Content Security Policy (requires django-csp middleware)
INSTALLED_APPS += [
    'csp',
]

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
]

# Example CSP policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_CONNECT_SRC = ("'self'",)
