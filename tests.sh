#!/usr/bin/env bash

python tests.py
cd tmp
chmod +x manage.py
echo "SECRET_KEY = 'secretkeytest'" > project_name/settings/local.py
pip install -r requirements_dev.txt --upgrade
./manage.py migrate
./manage.py init_data
./mange.py test
