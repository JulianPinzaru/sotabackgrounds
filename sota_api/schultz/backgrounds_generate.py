# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

"""Generate images using pretrained network pickle."""

import os
import re
from typing import List, Optional

import numpy as np
import PIL.Image
import torch

import base64
from io import BytesIO
import random


# ---------------------------------------------------------------------------
def num_range(s: str) -> List[int]:
    '''Accept either a comma separated list of numbers 'a,b,c' or a range 'a-c' and return as a list of ints.'''

    range_re = re.compile(r'^(\d+)-(\d+)$')
    m = range_re.match(s)
    if m:
        return list(range(int(m.group(1)), int(m.group(2)) + 1))
    vals = s.split(',')
    return [int(x) for x in vals]


def valmap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

# ----------------------------------------------------------------------------

# @click.command()
# @click.pass_context
# @click.option('--class', 'class_idx', type=int, help='Class label (unconditional if not specified)')
# @click.option('--noise-mode', help='Noise mode', type=click.Choice(['const', 'random', 'none']), default='const',
#               show_default=True)
# @click.option('--outdir', help='Where to save the output images', type=str, required=True, metavar='DIR')
# @click.option('--process', type=click.Choice(['image', 'interpolation', 'truncation']), default='image',
#               help='generation method', required=True)
# @click.option('--seeds', type=num_range, help='List of random seeds')
# @click.option('--trunc', 'truncation_psi', type=float, help='Truncation psi', default=1, show_default=True)
def generate_images(
        device,
        generator,
        process: str,
        # diameter: Optional[float],
        seeds: Optional[List[int]],
        # space: str,
        truncation_psi: float,
        noise_mode: str,
        outdir: str,
        class_idx: Optional[int],
    ):

    G = generator
    os.makedirs(outdir, exist_ok=True)

    # Labels.
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            return 'Must specify class label with --class when using a conditional network'
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print('warn: --class=lbl ignored when running on an unconditional network')

    if (process == 'image'):
        if seeds is None:
            return '--seeds option is required when not using --projected-w'

        # Generate images.
        for seed_idx, seed in enumerate(seeds):
            print('Generating image for seed %d (%d/%d) ...' % (seed, seed_idx, len(seeds)))
            z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
            # img = G(z, label, truncation_psi=truncation_psi, noise_mode=noise_mode, force_fp32=True)
            img = G(z, label, truncation_psi=truncation_psi, noise_mode=noise_mode)
            img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
            pil_img = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')
            buffered = BytesIO()
            # pil_img.save(f'{outdir}/seed{seed:04d}{random.randint(0,9999999)}.png')
            pil_img.save(buffered, format="JPEG")
            img_base64 = base64.b64encode(buffered.getvalue())
            img_base64 = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_base64
            img_base64_str = img_base64.decode('utf-8')
            return img_base64_str
