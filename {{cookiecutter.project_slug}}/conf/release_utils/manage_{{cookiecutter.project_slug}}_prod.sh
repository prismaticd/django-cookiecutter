#!/bin/bash

FOLDER_NAME="{{cookiecutter.project_slug}}_prod"
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
        git checkout master
        cp "../../conf/$FOLDER_NAME.env" .
        cp "../../conf/docker-compose-$FOLDER_NAME.yml" docker-compose.yml
        echo "Restart docker"
        select yn in "Yes" "No"; do
            case $yn in
                Yes ) sudo docker-compose up --build -d; break;;
                No ) exit;;
            esac
        done
        #curl -X POST -H 'Content-type: application/json' --data '{"text": "New Website version released in production!", "channel": "#dev", "username": "monkey-bot", "icon_emoji": ":monkey_face:"}' https://hooks.slack.com/services/
        echo "\nMigrate ?"
        select yn in "Yes" "No"; do
            case $yn in
                Yes ) sudo docker-compose run web1 manage migrate; break;;
                No ) echo "ok"; break;;
            esac
        done
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

echo "Usage -> 'update' or 'logs' or 'manage' or 'bash'"

