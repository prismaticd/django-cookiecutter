#!/usr/bin/env bash

cwd=$(pwd)

export DJANGO_SETTINGS_MODULE="project_name.settings.test"
export DATABASE_VENDOR="sqlite"
export DJANGO_LOG_LEVEL="WARNING"

rm -rf ./tmp/
cookiecutter --no-input --output-dir="./tmp/" .
cd tmp
cd project_name
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic --noinput --clear
./manage.py init_data
./manage.py test

cd $cwd
rm -rf ./tmp/
cookiecutter --no-input --output-dir="./tmp/" --config-file=cookiecutter-with-wagtail.yml .
cd tmp
cd project_name
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic --noinput --clear
./manage.py init_data
./manage.py test
./manage.py behave