#!/usr/bin/env bash

if [ "$TARGET" = "production" ]
then
	exec /usr/bin/supervisord
else 
	npm run serve -- --port 8080;
fi
