
[![Coverage report](https://gitlab.com/{{cookiecutter.gitlab_group}}/{{cookiecutter.gitlab_project_slug}}/badges/master/coverage.svg)](https://{{cookiecutter.gitlab_group}}.gitlab.io/{{cookiecutter.gitlab_project_slug}}/index.html)

# Dev install

```
git clone git@gitlab.com:{{cookiecutter.gitlab_group}}/{{cookiecutter.gitlab_project_slug}}.git
cd {{cookiecutter.gitlab_project_slug}}
pip install -r requirements_dev.txt --upgrade
echo "SECRET_KEY = 'randomstring'" >> {{cookiecutter.project_slug}}/settings/local.py
./manage.py migrate
./manage.py init_data
```

# Code formatting style

This project is using the python code formatter `black` (with line length override).

Basic usage:

```bash
black {{cookiecutter.project_slug}}
```

See https://github.com/ambv/black

Configuration defaults are in `pyproject.toml` - see https://github.com/ambv/black#configuration-format


# Useful dev commands / config

## CSS/JS pipeline

* node 8.x required
* npm install
* gulp watch

## Dev update

```
git pull && pip install -r requirements_dev.txt --upgrade && npm update  && python manage.py migrate
```

## One-liner to reset (sqlite) dev database
```
rm db.sqlite3 -f && python manage.py makemigrations && python manage.py migrate && python manage.py init_data
```

{% if cookiecutter.database_type == "postgres" %}
## To run postgres in dev

```
docker run -p 5432:5432 postgres:latest
```

Add something like this to your `settings/local.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB", 'postgres'),
        'USER': os.environ.get("POSTGRES_USER", 'postgres'),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", ''),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '5432'),
    }
}
```
{% elif cookiecutter.database_type == "mysql" %}
## To run mysql in dev

Create database command
```
CREATE DATABASE {{cookiecutter.project_slug}} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```


Add something like this to your `settings/local.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DATABASE", '{{cookiecutter.project_slug}}'),
        'USER': os.environ.get("MYSQL_USER", 'root'),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD", ''),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '3306'),
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'",
        },
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci"},
    }
}
```
{% endif %}

{% if cookiecutter.install_allauth == "y" %}
## Social login in dev

Get the OAuth clientid/secret for the relevant app and add the following to local.py before running `python manage.py init_data`
(or add them in admin afterwards)

```
INIT_AUTH_FACEBOOK_CLIENT_ID = 'todo'
INIT_AUTH_FACEBOOK_SECRET_KEY = 'todo'

INIT_AUTH_GOOGLE_CLIENT_ID = 'todo'
INIT_AUTH_GOOGLE_SECRET_KEY = 'todo'

```
{% endif %}


## Seeding random values

To explicitly set a random seed (used by both `manage.py init_data` and tests)

```bash
export PYTHON_RANDOM_SEED=123
```

Or to choose a random seed and print it.

```bash
export PYTHON_RANDOM_SEED=random
```

### Searching for a random failure

To find a seed that's causing failures, this is a useful bash script.  Change the test command to be as specific as you can in order to get to a quickly reproducible error:

```
echo "Searching for failing seed"; while [[ $? == 0 ]]; do export PYTHON_RANDOM_SEED=$RANDOM; ./manage.py test; done; echo "found failing seed $PYTHON_RANDOM_SEED"
```

## To run coverage locally

 ```
 pip install coverage
 coverage run --source='{{cookiecutter.project_slug}}/' manage.py test
 coverage report
 coverage html -d ./coverage
 cd coverage
 python -m SimpleHTTPServer 7500
 open localhost:7500
 ```


##  To check static typing
```
mypy --ignore-missing-imports -p  {{cookiecutter.project_slug}}
```

## To refresh the project from our cookiecutter template

This assumes the project is checked out to the directory {{cookiecutter.project_slug}}.

Beware, this will overwrite local files, check in or stash your changes before running.
```
pip install cookiecutter
cookiecutter https://github.com/prismaticd/django-cookiecutter/ --config-file conf/cookiecutter-config.yml --output-dir .. --overwrite-if-exists  --no-input
```
