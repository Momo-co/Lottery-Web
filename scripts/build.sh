#!/bin/bash

# Build Images
docker-compose build --parallel &&

# Push Image
docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}
docker-compose push