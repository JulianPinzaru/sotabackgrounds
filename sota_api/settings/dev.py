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

RUN_ON_CPU = os.getenv('RUN_ON_CPU', False)

MODEL_PATH_BACKGROUNDS = pathlib.Path(
    './schultz/networks/backgrounds1280x768/backgrounds1280x768-1280x768-3740.pkl')

network_pkl_backgrounds = str(MODEL_PATH_BACKGROUNDS)
print('Loading networks from "%s"...' % network_pkl_backgrounds)

if RUN_ON_CPU:
    DEVICE = torch.device('cpu')
else:
    DEVICE = torch.device('cuda')

f = dnnlib.util.open_url(network_pkl_backgrounds)
BACKGROUNDS_MODEL = legacy.load_network_pkl(f)['G_ema'].to(DEVICE)  # type: ignore
f.close()
MODEL_PATH_UNIVERSE = pathlib.Path(
    './schultz/networks/universe1280x768/universe-1280x768-2800.pkl')
network_pkl_universe = str(MODEL_PATH_UNIVERSE)


print('Loading networks from "%s"...' % network_pkl_universe)
f = dnnlib.util.open_url(network_pkl_universe)
UNIVERSE_MODEL = legacy.load_network_pkl(f)['G_ema'].to(DEVICE)  # type: ignore
f.close()
