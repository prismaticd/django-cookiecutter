#!/bin/bash

FOLDER_NAME="{{cookiecutter.project_slug}}_staging"
REPOSRC="git@gitlab.com:{{cookiecutter.gitlab_group}}/{{cookiecutter.gitlab_project_slug}}.git"
BRANCH=master

mkdir projects -p
cd projects
mkdir $FOLDER_NAME -p


if [ ! -d $FOLDER_NAME"/.git" ]
then
    git clone $REPOSRC $FOLDER_NAME
    cd $FOLDER_NAME
else
    cd $FOLDER_NAME
    git pull
fi



case "$1" in
'update')
    docker pull bchabord/django-nginx
    git checkout $BRANCH
    cp "../../conf/$FOLDER_NAME.env" .
    cp "../../conf/docker-compose-$FOLDER_NAME.yml" docker-compose.yml
    sudo docker-compose up --build -d
    curl -X POST -H 'Content-type: application/json' --data '{"text": "New Website version released in staging!", "channel": "#dev", "username": "monkey-bot", "icon_emoji": ":monkey_face:"}' https://hooks.slack.com/services/
    sudo docker-compose run web1 manage migrate
;;
'logs')
  sudo docker-compose logs -f --tail=50
;;
'manage')
   sudo docker-compose run web1 manage "${@:2}"
;;
'bash')
   sudo docker-compose run web1 /bin/bash
;;
esac




