FROM python:3.9.8-buster 
#https://jonnung.dev/docker/2020/04/08/optimizing-docker-images/
MAINTAINER Collector

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
COPY ./requirements.txt /backend/
# RUN apt add --update --no-cache postgresql-client
# RUN apt add --update --no-cache --virtual .tmp-build-deps \
#         gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
#pip으로 requirements.txt 설치함
# RUN apt del .tmp-build-deps

#/app을 기본 디렉토리로 설정함
COPY . /backend/
#프로젝트에서 만든 코드를 docker image에 복사해 준다. cf) ADD
EXPOSE 8000
