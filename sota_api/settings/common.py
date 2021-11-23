import os
import pathlib
import sys

sys.path.insert(1, './schultz/')
# insert at 1, 0 is the script path (or '' in REPL)

import torch
import dnnlib
import legacy
import training.augment


# TODO: RUN THIS IN DOCKER CONTAINER AND TRY USE AMD 24 CORE CPU.
# TODO: RUN THIS IN DOCKER SWARM MAYBE FOR PARALLELISM AND CONCURRENCY ?
# TODO: TRY TO MAKE THE IMAGE GENERATION CODE ASYNC -
# https://fastapi.tiangolo.com/async/#in-a-hurry
# https://docs.python.org/3/library/asyncio-task.html
