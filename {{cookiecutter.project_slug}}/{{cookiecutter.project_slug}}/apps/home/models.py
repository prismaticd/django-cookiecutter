# -*- coding: utf-8 -*-

from .apps import HomeConfig
{% if cookiecutter.install_wagtail == "y" %}
from django.db import models

from wagtail.wagtailcore import blocks

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class HomePage(Page):
    parent_page_types = []
    subpage_types = []

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('link', blocks.URLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
{% endif %}