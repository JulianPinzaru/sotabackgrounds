import os
import pathlib
import sys

sys.path.insert(1, './schultz/')
# insert at 1, 0 is the script path (or '' in REPL)

import torch
import dnnlib
import legacy
import training.augment

RUN_ON_CPU = os.getenv("RUN_ON_CPU", True)

MODEL_PATH_BACKGROUNDS = pathlib.Path(
	"./schultz/networks/backgrounds1280x768/backgrounds1280x768-1280x768-1280.pkl")

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
	"./schultz/networks/universe1280x768/universe-1280x768-fixed-aug-0.5-3020.pkl")
network_pkl_universe = str(MODEL_PATH_UNIVERSE)


print('Loading networks from "%s"...' % network_pkl_universe)
f = dnnlib.util.open_url(network_pkl_universe)
UNIVERSE_MODEL = legacy.load_network_pkl(f)['G_ema'].to(DEVICE)  # type: ignore
f.close()





# TODO: RUN THIS IN DOCKER CONTAINER AND TRY USE AMD 24 CORE CPU.
# TODO: RUN THIS IN DOCKER SWARM MAYBE FOR PARALLELISM AND CONCURRENCY ?
# TODO: TRY TO MAKE THE IMAGE GENERATION CODE ASYNC -
# https://fastapi.tiangolo.com/async/#in-a-hurry
# https://docs.python.org/3/library/asyncio-task.html
