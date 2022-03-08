FROM ubuntu:latest
LABEL maintainer="hjKim <yourmyeden@gmail.com>"

ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ curl

RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

RUN apt-get install -y python3-pip python3-dev

RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip install --upgrade pip
# apt clean
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/*
#FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app/

ENV FLASK_ENV=production
# uWSGI depends on C compiler
RUN apt update -y && \
  apt install gcc -y   

# dependencies Install
RUN pip install --no-cache-dir -r requirements.txt;

EXPOSE 5000

# uWSGI 시작 명령어
CMD gunicorn -c ./config.py