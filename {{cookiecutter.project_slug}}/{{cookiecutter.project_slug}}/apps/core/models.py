# -*- coding: utf-8 -*-

{% if cookiecutter.install_wagtail == "y" -%}
from typing import List

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    parent_page_types = []  # type: List[str]
    subpage_types = []  # type: List[str]

    body = StreamField([
        ("heading", blocks.CharBlock(classname="full title")),
        ("paragraph", blocks.RichTextBlock()),
        ("image", ImageChooserBlock()),
        ("link", blocks.URLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
{% endif %}