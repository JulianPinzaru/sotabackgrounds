#!/bin/bash
DIR="./venv"
if [ -d "$DIR" ]; then
	source ./venv/bin/activate;
fi
pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
