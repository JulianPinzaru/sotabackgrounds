#!/usr/bin/env bash

unset TORCH_CUDA_ARCH_LIST

if [ "$TARGET" = "production" ]
then
	exec /usr/bin/supervisord
else
	uvicorn main:app --reload --port 8001
fi
