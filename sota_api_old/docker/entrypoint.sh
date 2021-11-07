#!/usr/bin/env bash

unset TORCH_CUDA_ARCH_LIST
python3 manage.py makemigrations --settings sota_api.settings
python3 manage.py migrate --settings sota_api.settings

if [ "$TARGET" = "production" ]
then
	exec /usr/bin/supervisord
else
	python3 manage.py runserver 0.0.0.0:8000
fi
