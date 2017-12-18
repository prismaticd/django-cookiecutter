from django import template

register = template.Library()


@register.simple_tag
def get_user_primary_email(user):
    return user.emailaddress_set.get_primary(user=user)


@register.simple_tag
def get_user_other_emails(user):
    return user.emailaddress_set.filter(primary=False)
