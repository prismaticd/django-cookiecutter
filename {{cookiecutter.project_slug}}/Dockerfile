FROM prismaticd/django-nginx:3

EXPOSE 9808

WORKDIR /files/
COPY ./entrypoint.sh /files/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/nginx_{{cookiecutter.project_slug}}.conf /etc/nginx/conf.d/{{cookiecutter.project_slug}}.conf
COPY conf/ /files/conf

RUN chmod +x entrypoint.sh && nginx -t

COPY ./requirements.txt /files/requirements.txt
COPY ./{{cookiecutter.project_slug}}/requirements/ /files/{{cookiecutter.project_slug}}/requirements/

RUN pip install -r requirements.txt && pip install awscli && rm -rf /root/.cache/

COPY ./ /files/


