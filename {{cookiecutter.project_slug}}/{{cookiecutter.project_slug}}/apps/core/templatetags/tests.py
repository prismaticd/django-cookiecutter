from django.template import Context, Template
from django.test import TestCase


class TestTags(TestCase):

    def render_template(self, string, context=None):
        """
        helper function for template tag testing, from https://stackoverflow.com/a/1690879/
        :param string:
        :param context:
        :return:
        """

        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_define(self):
{%- raw %}
        template = """
        {% load myfilters %}
        {% if item %}
           {% define "Edit" as action %}
        {% else %}
           {% define "Create" as action %}
        {% endif %}
        Would you like to {{action}} this item
        """
{%- endraw %}

        expected_default = "Would you like to Create this item"

        self.assertHTMLEqual(self.render_template(template), expected_default)
        self.assertHTMLEqual(self.render_template(template, context={"item": False}), expected_default)
        self.assertHTMLEqual(self.render_template(template, context={"item": True}), "Would you like to Edit this item")
