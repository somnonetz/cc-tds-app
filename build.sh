#!/usr/bin/env bash

REGISTRY_URL=docker.io/curiouscontainers/cc-tds-app
TAG=0.11

docker pull docker.io/curiouscontainers/cc-image-debian:${TAG}
docker pull ${REGISTRY_URL}
docker build -t ${REGISTRY_URL} .
docker push ${REGISTRY_URL}

if [[ ! -z ${TAG} ]]; then
    docker tag ${REGISTRY_URL} ${REGISTRY_URL}:${TAG}
    docker push ${REGISTRY_URL}:${TAG}
fi
