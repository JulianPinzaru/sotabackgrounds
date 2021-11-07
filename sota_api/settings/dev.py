from .common import *

# Local Dev overrides
DEBUG = True
LOG_LEVEL = DEBUG

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    # "https://example.com",
    # "https://sub.example.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://24.21.90.246:8000"
]

from logging.config import dictConfig
from .logconfig import LogConfig

dictConfig(LogConfig(LOG_LEVEL=LOG_LEVEL).dict())
