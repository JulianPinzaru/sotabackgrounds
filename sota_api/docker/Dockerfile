FROM nvcr.io/nvidia/pytorch:20.12-py3

LABEL maintainer="wx"

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install imageio-ffmpeg==0.4.3 pyspng==0.1.0

WORKDIR /workspace

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -o Acquire::Queue-mode=access install --no-install-recommends -y \
  gcc \
  wget \
  curl \
  supervisor \
  nginx \
  cron \
  libssl-dev \
  libcurl4-openssl-dev \
  libpq-dev \
  libxml2-dev \
  libxslt1-dev \
  libffi-dev \
  libjpeg-dev \
  zlib1g-dev \
  apt-transport-https \
  ca-certificates \
  gnupg2 \
  software-properties-common

COPY ./requirements.txt /workspace/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /workspace
RUN mkdir -p ./public/logs
COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./docker/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["sh", "./docker/entrypoint.sh"]
