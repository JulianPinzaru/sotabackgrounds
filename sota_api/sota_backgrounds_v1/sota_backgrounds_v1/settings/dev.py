from .common import *

# Local Dev overrides
DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1', '0.0.0.0', 'localhost']

CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    # "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {  # 86,400 seconds in a day
    'anon': '2000/minute', 'user': '10000000/day',
}
