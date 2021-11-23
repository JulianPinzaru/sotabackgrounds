from .common import *

# Production overrides
DEBUG = False
LOG_LEVEL = DEBUG

ALLOWED_HOSTS = ['*', ]

from logging.config import dictConfig
from .logconfig import LogConfig

dictConfig(LogConfig(LOG_LEVEL=LOG_LEVEL).dict())

RUN_ON_CPU = os.getenv('RUN_ON_CPU', False)

MODEL_PATH_BACKGROUNDS = pathlib.Path(
	'/data/networks/backgrounds1280x768/backgrounds1280x768-1280x768-2820.pkl')

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
	'/data/networks/universe1280x768/universe-1280x768-3420.pkl')
network_pkl_universe = str(MODEL_PATH_UNIVERSE)


print('Loading networks from "%s"...' % network_pkl_universe)
f = dnnlib.util.open_url(network_pkl_universe)
UNIVERSE_MODEL = legacy.load_network_pkl(f)['G_ema'].to(DEVICE)  # type: ignore
f.close()
