from typing import Optional
from enum import Enum

from fastapi import FastAPI, Request

import uvicorn
import logging

from models import GeneratorModel
from schultz.backgrounds_generate import generate_images
import settings

logger = logging.getLogger("sota_api")

app = FastAPI()


@app.get('/model')
def get_status():
	return {'running': True}


@app.post("/model")
async def generate(generator_params: GeneratorModel):
	logger.info("Generating image for params: ", generator_params.dict())
	network = generator_params.network
	DEVICE = settings.DEVICE
	if network == 'universe_generator':
		GENERATOR = settings.UNIVERSE_MODEL
	elif network == 'backgrounds_generator':
		GENERATOR = settings.BACKGROUNDS_MODEL
	else:
		raise Exception('no generator')
	try:
		img_base64_str = generate_images(
			device=DEVICE,
			generator=GENERATOR,
			process='image',
			seeds=generator_params.seeds,
			truncation_psi=generator_params.truncation_psi,
			noise_mode=generator_params.noise_mode,  # random , None
			outdir='out',
			class_idx=generator_params.class_idx,
			is_cpu=settings.RUN_ON_CPU)
		response = {'image': img_base64_str}
	except Exception as ex:
		logger.error(ex)
		return {}
	return response

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8001)
