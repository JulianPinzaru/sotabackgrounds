from .common import *

# Production overrides
DEBUG = False
LOG_LEVEL = DEBUG

ALLOWED_HOSTS = ['*', ]

from logging.config import dictConfig
from .logconfig import LogConfig

dictConfig(LogConfig(LOG_LEVEL=LOG_LEVEL).dict())
