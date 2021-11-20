FROM node:16.13.0-buster

MAINTAINER Collector

RUN mkdir /frontend
WORKDIR /frontend

COPY ./package.json ./
COPY ./yarn.lock ./
WORKDIR /frontend/
RUN npm install 
RUN npm install -g expo-cli



EXPOSE 19000
EXPOSE 19001
EXPOSE 19002
COPY . /frontend/