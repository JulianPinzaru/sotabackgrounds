FROM python:3.8-buster

LABEL maintainer="wx"

RUN apt-get update && apt-get -o Acquire::Queue-mode=access install --no-install-recommends -y \
  gcc \
  git \
  wget \
  curl \
  nano \
  supervisor \
  nginx \
  cron \
  libssl-dev \
  libcurl4-openssl-dev \
  libpq-dev \
  libxml2-dev \
  libxslt1-dev \
  net-tools \
  libffi-dev \
  libjpeg-dev \
  libjpeg62-turbo \
  libjpeg62-turbo-dev \
  zlib1g-dev \
  \
  apt-transport-https \
  ca-certificates \
  gnupg2 \
  software-properties-common


RUN apt install openjdk-11-jdk -y
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /data
COPY ./requirements.txt /data/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /data

RUN mkdir -p ./public/logs
RUN mkdir -p ./public/media
RUN mkdir -p ./public/static
RUN mkdir -p ./private/static

COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./docker/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["sh", "./docker/entrypoint.sh"]
