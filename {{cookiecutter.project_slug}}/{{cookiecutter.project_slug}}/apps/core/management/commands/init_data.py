import json
import os
import random

{% if cookiecutter.install_allauth == "y" -%}
from allauth.socialaccount.models import SocialApp
{% endif %}
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site as DjangoSite
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

{% if cookiecutter.install_wagtail == "y" -%}
from wagtail.core.models import Page, Site as WagtailSite, ContentType
{%- endif %}
{% if cookiecutter.install_wagtail == "y" %}
from ...models import HomePage
{%- endif %}

random.seed(123456789)

{% if cookiecutter.install_wagtail == "y" %}
def generate_body(nb_iterations):
    return_array = []

    for _ in range(nb_iterations):
        return_array.append({"type": "heading", "value": lorem_ipsum.words(random.randint(2, 6), common=False)})
        return_array.append({"type": "paragraph", "value": "<p>{}</p>".format(lorem_ipsum.paragraph())})
        return_array.append({"type": "paragraph", "value": "<p>{}</p>".format(lorem_ipsum.paragraph())})

    return return_array
{% endif %}

class Command(BaseCommand):
    help = "Create the what is need to run the site"
{% if cookiecutter.install_wagtail == "y" %}
    def add_arguments(self, parser):
        parser.add_argument("--nb_objects", default=50, type=int)

    def read_fixture(self, fixture_path, nb=0):
        with open(os.path.join(settings.BASE_DIR, fixture_path)) as f:
            data = json.load(f)
            return data[nb].get("fields")

    def create_page_type_if_not_exists(self, current_home_page, page_type, slug, heading, defaults=None):
        if not defaults:
            defaults = {}
        # CaseStudyPage, PricingPage, ContactPage, ExpertisePage
        has_page = False
        content_type = ContentType.objects.get_for_model(page_type)
        for home_page_descendants in current_home_page.get_descendants():
            if home_page_descendants.content_type == content_type:
                has_page = True

        if not has_page:
            new_page = page_type(slug=slug, title=heading, **defaults)
            # new_page.body = [
            #     {"type": "heading", "value": "{}".format(heading)},
            #     {"type": "paragraph", "value": "<p>{}</p>".format(body)}
            # ]
            current_home_page.add_child(instance=new_page)
            new_page.save_revision().publish()

            return new_page
{% endif %}
    def handle(self, *args, **options):
{%- if cookiecutter.install_wagtail == "y" %}
        nb_objects = options["nb_objects"]
{%- endif %}

        site = DjangoSite.objects.get(id=settings.SITE_ID)
        site.domain = "{{ cookiecutter.prod_host }}"
        site.name = "{{ cookiecutter.project_name }}"
        site.save()

        super_user = User.objects.filter(is_superuser=1).first()
        if not super_user:
            print("No Super user creating default admin")
            User.objects.create_superuser(username="admin", password="adminadmin", email="")
{% if cookiecutter.install_wagtail == "y" %}
        root_page = Page.objects.get(slug="root")

        main_site = WagtailSite.objects.get(is_default_site=1)

        main_site.hostname = site.domain
        main_site.site_name = site.name
        main_site.save()

        current_home_page = main_site.root_page
        if current_home_page.content_type_id == 1:
            print("No Homepage, creating default")
            new_home_page = HomePage(slug="{{cookiecutter.project_slug}}-home", title="{{cookiecutter.project_name}} HomePage")
            root_page.add_child(instance=new_home_page)
            new_home_page.save_revision().publish()
            main_site.root_page = new_home_page
            main_site.save()
            current_home_page.delete()
            current_home_page = new_home_page
{% endif %}

{%- if cookiecutter.install_allauth == "y" %}
        if len(SocialApp.objects.all()) == 0:
            print("No Social Apps, creating defaults")
            facebook = SocialApp(provider="facebook",
                                 name="Facebook Oauth",
                                 client_id=getattr(settings, "INIT_AUTH_FACEBOOK_CLIENT_ID", "changeme"),
                                 secret=getattr(settings, "INIT_AUTH_FACEBOOK_SECRET_KEY", "changeme"))
            facebook.save()
            facebook.sites.add(1)
            google = SocialApp(provider="google",
                               name="Google Oauth",
                               client_id=getattr(settings, "INIT_AUTH_GOOGLE_CLIENT_ID", "changeme"),
                               secret=getattr(settings, "INIT_AUTH_GOOGLE_SECRET_KEY", "changeme"))
            google.save()
            google.sites.add(1)
{% endif -%}
