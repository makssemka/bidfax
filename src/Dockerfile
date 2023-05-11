FROM python:3.9 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y -q --no-install-recommends\
  build-essential \
  libpq-dev \
  iptables

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /home/bidfax/src/

COPY ./requirements/base.txt requirements/base.txt

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements/base.txt

RUN adduser --disabled-password bidfax-user

USER bidfax-user
