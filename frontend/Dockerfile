FROM node:16.13.0-alpine3.14

RUN mkdir /frontend
WORKDIR /frontend

RUN npm install axios
RUN npm install -g expo-cli
COPY ./package.json ./
COPY ./yarn.lock ./
WORKDIR /frontend/
RUN npm install 


EXPOSE 19000
EXPOSE 19001
EXPOSE 19002
COPY . /frontend/
