#!/bin/bash
set -e

source project_config.properties

if [ -f ../secrets/secrets.sh ]; then source ../secrets/secrets.sh; fi

if [ x${DOCKER_REPO} != x ]; then

  find ./ -name "__pycache__" | xargs rm -rf

  for DOCKER_TAG in ${DOCKER_TAGS[@]}; do
    docker build -t ${DOCKER_TAG} -t ${DOCKER_IMG}:${DOCKER_TAG} -t ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG} --target ${DOCKER_TAG} .
  done

  # We are pushing only the tags identified as tests in order to run unit testing, integration testing...
  for DOCKER_TAG in ${DOCKER_TEST_TAGS[@]}; do
    docker build -t ${DOCKER_TAG} -t ${DOCKER_IMG}:${DOCKER_TAG} -t ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG} --target ${DOCKER_TAG} .

    aws ecr get-login-password --region ${AWS_ECR_REGION} | docker login --username AWS --password-stdin ${DOCKER_REPO}
    docker push ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}
  done
fi