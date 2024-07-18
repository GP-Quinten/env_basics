#!/bin/bash
set -e

source project_config.properties

if [ -f ../secrets/secrets.sh ]; then source ../secrets/secrets.sh; fi

TAG=$(echo ${GIT_BRANCH} | grep tags | sed -e "s#.*/tags/\(.*\)#\1#")

if [ -z ${TAG} ]; then echo "Could not identify tag"; exit 1; else echo "Tag is set to ${TAG}"; fi

if [ x${DOCKER_REPO} != x ]; then
  aws ecr get-login-password --region ${AWS_ECR_REGION} | docker login --username AWS --password-stdin ${DOCKER_REPO}

  find ./ -name "__pycache__" | xargs rm -rf

  for DOCKER_TAG in ${DOCKER_TAGS[@]}; do
    docker build -t ${DOCKER_TAG} -t ${DOCKER_IMG}:${DOCKER_TAG} -t ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG} -t ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}_prod -t ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}_${TAG} --target ${DOCKER_TAG} .

    docker push ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}_${TAG}
    docker push ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}_prod
  done
fi
