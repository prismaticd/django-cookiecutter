#!/usr/bin/env bash

cwd=$(pwd)

rm -rf ./tmp/
cookiecutter --no-input --output-dir="./tmp/" .
cd tmp
cd project_name
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py migrate
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
./manage.py migrate
./manage.py init_data
./manage.py test
