#!/bin/bash
set -e

source project_config.properties

if [ -f ../secrets/secrets.sh ]; then source ../secrets/secrets.sh; fi

if [ x${DOCKER_REPO} != x ]; then
  aws ecr get-login-password --region ${AWS_ECR_REGION} | docker login --username AWS --password-stdin ${DOCKER_REPO}

  for DOCKER_TAG in ${DOCKER_TAGS[@]}; do
    docker push ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}
  done
fi