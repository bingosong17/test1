#!/bin/bash

# ENV=${1}
IMAGE_NAME="ppyautotest"

#if [ ! -d $WORKSPACE/node_modules ] ; then
#docker run --rm -v /mnt/npm:/npm   \
#	-v /mnt/jenkins_home/workspace/$JOB_NAME:/var/project -w /var/project/$WORK_NAME \
#	node:10 	npm install -S
#
#if [ $? -eq 0 ]; then
#echo "node install succ"
#else
#echo "node install fail exit"
#exit 1
#fi
#
#fi



#build
# docker run --rm -v /mnt/npm:/npm   \
#	-v /mnt/jenkins_home/workspace/$JOB_NAME:/var/project -w /var/project/$WORK_NAME \
#	node:10  npm run build
# --rm用来调试，退出即删除



docker build -f dockerfile . -t bingo/${IMAGE_NAME}
if [ $? -eq 0 ]; then
echo "docker build succ"
else
echo "docker build fail exit"
exit 1
fi