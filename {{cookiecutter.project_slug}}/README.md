
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
rm db.sqlite3 && python manage.py makemigrations && python manage.py migrate && python manage.py init_data
```

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
