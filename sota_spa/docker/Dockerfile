FROM node:14.17.3-stretch
MAINTAINER Iulian Pinzaru "pinzaru.iulian.igor@gmail.com"

WORKDIR /data
ARG TARGET

# Install python, pip and python packages

RUN apt-get update && apt-get -o Acquire::Queue-mode=access install --no-install-recommends -y \
  gcc \
  wget \
  curl \
  nano \
  supervisor \
  nginx \
  cron \
  libssl-dev \
  libcurl4-openssl-dev \
  apt-transport-https \
  ca-certificates \
  gnupg2 \
  software-properties-common

# Run the following commands for deployment

COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./docker/nginx.conf /etc/nginx/nginx.conf

COPY . /data
COPY package*.json ./

RUN npm install --save-prod

RUN if [ "$TARGET" = "production" ] ; then npm run build; fi;

# Remove unused directories and files, except the once built for nginx sharing the app and docker dir (for production only)
RUN if [ "$TARGET" = "production" ] ; then /bin/bash -c 'find . -maxdepth 1 ! -path ./dist ! -path ./docker ! -path . -execdir rm -rf {} \;'; fi;

RUN mkdir -p /data/logs
EXPOSE 80
CMD ["sh", "./docker/entrypoint.sh"]




