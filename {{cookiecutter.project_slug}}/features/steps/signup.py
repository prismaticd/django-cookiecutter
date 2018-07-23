from behave import given, when, then
from django.core import mail

from features.hints import BehaveContext


@given("a new user")
def step_impl(context):
    """
    :param context:
    :return:
    """
    # raise NotImplementedError(u'STEP: Given a new user')
    pass


@when("they register using {auth_type}")
def step_impl(context: BehaveContext, auth_type):
    if auth_type == "email/password":
        context.response = context.test.client.post(
            "/auth/register/", data={"email": "test@test.com", "password1": "qwertyuiop", "password2": "qwertyuiop"}
        )
    else:
        raise NotImplementedError(u"STEP: When they register using {}".format(auth_type))


@when("set up their profile")
def step_impl(context: BehaveContext, auth_type):
    context.response = context.test.client.post("/profile/", data={"first_name": "first", "last_name": "last"})


@then("they need to confirm their email")
def step_impl(context: BehaveContext):
    """
    :param behave_django.environment.PatchedContext context:
    :return:
    """
    """:type: django.test.Response"""
    response = context.response  # type: django.test.Response
    context.test.assertEqual(len(mail.outbox), 1)
    context.test.assertIn("Confirm Your E-mail", mail.outbox[0].subject)
    # TODO - check that email confirm works + is required


@then("the user is on the page {url}")
def step_impl(context: BehaveContext, url):
    response = context.response
    context.test.assertEqual(response.status_code, 302)
    context.test.assertEqual(response.url, url)
    context.response = context.test.client.get(response.url)


@then("the user has a {thing}")
def step_impl(context: BehaveContext, thing: str):
    response = context.response  # type: django.test.Responser
    if thing == "profile":
        context.test.assertIsNotNone(response.context["user"].profile)
    elif thing == "generated_email":
        context.test.assertIsNot(response.context["user"].profile.generated_email)
    elif thing == "rule_id":
        context.test.assertIsNotNone(response.context["user"].profile.rule_id)
    else:
        raise NotImplementedError(u"STEP:the user has a {thing}".format(thing))


@then("they don't need to confirm their email")
def step_impl(context: BehaveContext):
    context.test.assertEqual(len(mail.outbox), 0)
