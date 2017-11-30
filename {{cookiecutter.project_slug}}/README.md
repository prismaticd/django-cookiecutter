
[![Coverage report](https://gitlab.com/{{cookiecutter.gitlab_group}}/{{cookiecutter.gitlab_project_slug}}/badges/master/coverage.svg)](https://{{cookiecutter.gitlab_group}}.gitlab.io/{{cookiecutter.gitlab_project_slug}}/index.html)

# Dev install

* git checkout git@gitlab.com:{{cookiecutter.gitlab_group}}/{{cookiecutter.gitlab_project_slug}}.git
* cd {{cookiecutter.gitlab_project_slug}}
* pip install -r requirements_dev.txt --upgrade
* create the {{cookiecutter.project_slug}}/settings/local.py with SECRET_KEY = 'randomstring'
* ./manage.py migrate
* ./manage.py init_data

# CSS/JS pipeline

* node 8.x required
* npm install
* gulp watch

# Dev update

* git pull && pip install -r requirements_dev.txt --upgrade && npm update  && python manage.py migrate


# Onliner to check migrations
```
rm db.sqlite3 && python manage.py makemigrations && python manage.py migrate && python manage.py init_data
```



To run coverage locally

 ```
 pip install coverage
 coverage run --source='{{cookiecutter.project_slug}}/' manage.py test
 coverage report
 coverage html -d ./coverage
 cd coverage
 python -m SimpleHTTPServer 7500
 open localhost:7500
 ```




#  To check static typing
```
mypy --ignore-missing-imports -p  {{cookiecutter.project_slug}}
```

# To refresh the project from our cookiecutter template

This assumes the project is checked out to the directory {{cookiecutter.project_slug}}.

Beware, this will overwrite local files, check in or stash your changes before running.
```
pip install cookiecutter
cookiecutter https://github.com/prismaticd/django-cookiecutter/ --overwrite-if-exists --output-dir .. conf/cookiecutter-config.yml --no-input
```
