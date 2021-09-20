#!/bin/sh

cd .. || exit

# shellcheck disable=SC2046ß
docker stop $(docker ps -qa)

cd backup_test || exit
git fetch origin main
git pull origin main --force

docker build -t alexprotchenko/backup-service .

docker push alexprotchenko/backup-service

docker run -d --rm -p 82.148.19.206:8080:8080 alexprotchenko/backup-service