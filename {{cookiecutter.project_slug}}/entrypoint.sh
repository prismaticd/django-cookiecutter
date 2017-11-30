#!/usr/bin/env bash

# -e exit on non 0 return
set -e
# -u exit on undefined variables
set -u
# -x print command before running
set -x
# bubble up the non 0 on pipes
set -o pipefail

echo "Launching Entrypoint"
if [[ ! -v DJANGO_SETTINGS_MODULE ]]; then
    export DJANGO_SETTINGS_MODULE="{{cookiecutter.project_slug}}.settings.prod"
fi

#function inject_env {
#  ${CONFIG_URL?"Need to set CONFIG_URL env variable"}
#  ${CONFIG_URL:?"Need to set CONFIG_URL env variable not empty"}
#  aws s3 cp $CONFIG_URL /tmp/env_config
#  export $(cat /tmp/env_config | grep -v ^# | grep '=' | xargs)
#  rm /tmp/env_config
#}

if [[ $# -eq 0 ]]; then
  #inject_env
    exit 0
else
  if [[ $1 == "" ]]; then
   exit 0
  elif [[ $1 == "prod" ]]; then
    echo "Webserver: Executing $DJANGO_SETTINGS_MODULE"
    service nginx start
    python manage.py collectstatic --noinput --clear
    uwsgi --ini conf/uwsgi.conf
  elif  [[ $1 == "test" ]]; then
    export DJANGO_SETTINGS_MODULE="{{cookiecutter.project_slug}}.settings.test"
    export DJANGO_LOG_LEVEL="WARNING"

    echo "Validate nginx config"
    service nginx start

    pip install -r {{cookiecutter.project_slug}}/requirements/test.txt
    echo "Checking for missing migrations"
    python manage.py makemigrations --check --dry-run

    python manage.py migrate
    rm -rf ./.static/
    python manage.py collectstatic --noinput --clear

    coverage run --source='{{cookiecutter.project_slug}}/' manage.py test
{%- if cookiecutter.install_behave_test == "y" %}
    coverage run --source='{{cookiecutter.project_slug}}/' --append manage.py behave
{%- endif %}

    coverage report
    coverage html -d ./coverage
  elif  [[ $1 == manage* ]]; then
    echo "Executing manage.py ${@:2}"
    python manage.py "${@:2}"
  else
    # For gitlab we need a non blocking entrypoint starting bash
    exec "$@"
  fi
fi

#export DJANGO_SETTINGS_MODULE="{{cookiecutter.project_slug}}.settings.production" && python manage.py migrate
