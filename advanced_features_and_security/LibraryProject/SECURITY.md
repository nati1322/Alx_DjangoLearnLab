# Security Best Practices in Django

## Secure Settings
- `DEBUG=False`: Hides sensitive error messages in production.
- `SECURE_SSL_REDIRECT=True`: Forces HTTPS.
- `SECURE_HSTS_SECONDS=31536000`: Enables HTTP Strict Transport Security.
- `SESSION_COOKIE_SECURE=True`: Prevents cookies from being sent over HTTP.

## CSRF Protection
- All forms include `{% csrf_token %}`.
- `CSRF_COOKIE_SECURE=True` ensures CSRF tokens are transmitted securely.

## SQL Injection Prevention
- No raw SQL queries are used.
- User inputs are validated and sanitized using Django ORM.

## Content Security Policy (CSP)
- `django-csp` is used to restrict content sources and prevent XSS.

## Security Testing
1. **CSRF Test**: Ensure forms cannot be submitted from unauthorized external websites.
2. **SQL Injection Test**: Try injecting SQL commands in search fields.
3. **XSS Test**: Attempt to insert `<script>alert('XSS')</script>` in inputs.
