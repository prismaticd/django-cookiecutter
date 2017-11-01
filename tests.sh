#!/usr/bin/env bash

rm -rf ./tmp/
cookiecutter --no_input --output_dir="./tmp/" .
cd tmp
cd project_name
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py migrate
./manage.py init_data
./manage.py test

rm -rf ./tmp/
cookiecutter --no_input --output_dir="./tmp/" --config-file=cookiecutter-with-wagtail.yml .
cd tmp
cd project_name
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py migrate
./manage.py init_data
./manage.py test
