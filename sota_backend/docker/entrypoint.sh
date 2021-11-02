#!/usr/bin/env bash

python3 manage.py makemigrations --settings backend.settings 
python3 manage.py migrate --settings backend.settings
python3 manage.py create_parquet_files --settings backend.settings
python3 manage.py store_parquet_to_database --settings backend.settings
python3 manage.py collectstatic --noinput --settings backend.settings

if [ "$TARGET" = "production" ]
then
	exec /usr/bin/supervisord
else 
	python3 manage.py runserver 0.0.0.0:8000
fi
