from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime
import random


def generate_default_seed():
	return [random.randint(0, 65536)]


class InferenceModelField(str, Enum):
	universe_generator = 'universe_generator'
	backgrounds_generator = 'backgrounds_generator'


class InferenceNoiseModeField(str, Enum):
	const = 'const'  # Constant Noise
	random = 'random'  # Random Noise
	none = 'none'  # No noise


class GeneratorModel(BaseModel):
	network: InferenceModelField = 'universe_generator'
	seeds: List[int] = Field(default_factory=generate_default_seed, ge=0, le=65536)
	truncation_psi: float = Field(ge=-3.0, le=3.0)
	noise_mode: InferenceNoiseModeField = 'random'
	class_idx: Optional[int] = Field(None, ge=0, le=2)

	@staticmethod
	def get_multiclass_networks():
		return ['backgrounds_generator']

	@validator('class_idx')
	def class_idx_validator(cls, v, values, **kwargs):
		if v is not None:
			if 'network' in values and values['network'] not in cls.get_multiclass_networks():
				raise ValueError('This model `{}` does not support class_idx.'.format(values['network']))
		if v is None and v in cls.get_multiclass_networks():
			raise ValueError('This model has to have a class selected.')
		return v

