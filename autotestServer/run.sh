#!/bin/bash

IMAGE_NAME="ppyautotest"

C_NAME=${1}

docker rm -f ${C_NAME}
# docker rmi bingo/${IMAGE_NAME}
# docker rmi $(docker images -f "dangling=true" -q)

docker run -d --restart=always -v /mnt/jenkins_home/workspace/httprunner:/usr/src/app/ppy --name=${C_NAME} -p 18801:8080   bingo/${IMAGE_NAME}