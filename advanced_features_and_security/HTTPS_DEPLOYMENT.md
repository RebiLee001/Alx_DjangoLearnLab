# HTTPS Deployment Configuration

This Django application is configured to enforce HTTPS for secure communication.

## Django Settings
The following settings are enabled in `settings.py`:

- `SECURE_SSL_REDIRECT = True`  
  Redirects all HTTP requests to HTTPS.

- `SECURE_HSTS_SECONDS = 31536000`  
  Enables HTTP Strict Transport Security for one year.

- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`  
  Applies HSTS to all subdomains.

- `SECURE_HSTS_PRELOAD = True`  
  Allows the site to be included in browser preload lists.

- `SESSION_COOKIE_SECURE = True`  
  Ensures session cookies are only sent over HTTPS.

- `CSRF_COOKIE_SECURE = True`  
  Ensures CSRF cookies are only sent over HTTPS.

- `X_FRAME_OPTIONS = "DENY"`  
  Prevents clickjacking.

- `SECURE_CONTENT_TYPE_NOSNIFF = True`  
  Prevents MIME-type sniffing.

- `SECURE_BROWSER_XSS_FILTER = True`  
  Enables browser XSS protection.

## Web Server Configuration (Example)
In production, HTTPS should be configured using a web server such as Nginx or Apache with valid SSL/TLS certificates (e.g., from Let's Encrypt).

