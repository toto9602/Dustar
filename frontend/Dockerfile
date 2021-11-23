FROM kerbe/expo:latest

USER root

RUN mkdir /frontend
WORKDIR /frontend

COPY ./package.json ./
COPY ./yarn.lock ./
WORKDIR /frontend/
RUN npm install 
# RUN npm install -g expo-cli

ENV EXPO_DEVTOOLS_LISTEN_ADDRESS=192.168.0.18
ENV REACT_NATIVE_PACKAGER_HOSTNAME=192.168.0.18
ENV EXPO_DEBUG=true

EXPOSE 19000
EXPOSE 19001
EXPOSE 19002
COPY . /frontend/