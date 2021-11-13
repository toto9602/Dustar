FROM node:latest

MAINTAINER Collector

RUN mkdir /frontend
WORKDIR /frontend
COPY ./package.json /frontend/package.json
COPY ./yarn.lock /frontend/yarn.lock

RUN npm install 
RUN npm install -g expo-cli

COPY ./ /frontend
