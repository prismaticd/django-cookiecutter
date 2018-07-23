from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(value, arg):
    #  Add a custom class to a form widget and add is-danger if there are errors
    if hasattr(value, "errors") and value.errors:
        arg = "is-danger " + arg
    return value.as_widget(attrs={"class": arg})


@register.assignment_tag
def define(val=None):
{% raw %}
    """
{% if item %}
   {% define "Edit" as action %}
{% else %}
   {% define "Create" as action %}
{% endif %}
Would you like to {{action}} this item
    """
{% endraw %}
    return val
