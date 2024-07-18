#!/bin/bash
set -e

source project_config.properties

if [ -f ../secrets/secrets_test_auto.sh ]; then source ../secrets/secrets_test_auto.sh; fi

# TODO: Make the tests runnable on non GPU servers
# check if nvidia gpu support is enabled on host
if ! [ -x "$(command -v nvidia-smi)" ]; then
  echo 'Error: nvidia drivers could not be found. Aborting.' >&2
  exit 1
fi

if [ x${DOCKER_REPO} != x ]; then
  aws ecr get-login-password --region ${AWS_ECR_REGION} | docker login --username AWS --password-stdin ${DOCKER_REPO}

  # We are pushing only the tags identified as tests in order to run unit testing, integration testing...
  for DOCKER_TAG in ${DOCKER_TEST_TAGS[@]}; do

    if [[ ${DOCKER_TAG} == *_gpu ]]; then
      # check if gpu support is enabled in docker image
      docker run --pull=always --gpus=all --entrypoint=/usr/bin/env --rm ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG} python3.8 -c 'import torch; import sys; sys.exit(not torch.cuda.is_available())'
      ret=$?
      if [ $ret != 0 ]; then
        echo 'Error: nvidia drivers could not be enabled in pytorch. Aborting.' >&2
        exit 1
      fi
    fi


    mkdir -p reports_${DOCKER_TAG}

    docker run -v "${PWD}/reports_${DOCKER_TAG}":/opt/project/reports --pull=always --rm --gpus=all --env-file=../secrets/secrets_test_auto.sh ${DOCKER_REPO}/${DOCKER_IMG}:${DOCKER_TAG}
  done
fi


