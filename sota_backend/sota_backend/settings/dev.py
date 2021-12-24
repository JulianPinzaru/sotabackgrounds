from .common import *

# Local Dev overrides
DEBUG = True

# ALLOWED_HOSTS = ['*', '127.0.0.1', '0.0.0.0', 'localhost']
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    # "https://sub.example.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://24.21.90.246:8000",
    "http://192.168.0.23:8000",
    "http://sotabackgrounds:8000"
]

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {  # 86,400 seconds in a day
    'anon': '2000/minute', 'user': '10000000/day',
}

CORS_ORIGIN_ALLOW_ALL = DEBUG

MODEL_DOMAIN = 'http://localhost:8001/'
