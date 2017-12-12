from features.hints import BehaveContext
import re
from behave import given, when, then
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
#from behave_django.environment import PatchedContext
# from behave_django.testcase import BehaviorDrivenTestCase
# from django.test import SimpleTestCase
from {{ cookiecutter.project_slug }}.apps.profile.models import Profile


# class BehaveContext(PatchedContext):
#     test: BehaviorDrivenTestCase


@given("a registered user")
def step_impl(context: BehaveContext):
    User = get_user_model()
    context.user = User()
    context.user.email = "foo@bar.com"
    context.user.username = "foo@bar.com"
    context.user.password = "qwertyuiop"
    context.user.save()

@when("they submit a password reset request")
def step_impl(context: BehaveContext):
    context.response = context.test.client.post("/auth/password/reset/", data={
        "email": context.user.email
    })

@when("the user logs in")
def step_impl(context: BehaveContext):
    context.response = context.test.client.post("/auth/login/", data={"email": "foo@bar.com", "password": "qwertyuiop"})


@then("they are sent a {email_type} email")
def step_impl(context: BehaveContext, email_type):
    """
    :type context: behave.runner.Context
    """
    response = context.response
    context.test.assertEqual(len(mail.outbox), 1)
    email = mail.outbox[0]

    if email_type == "password reset":
        subject_substring = "Password Reset"
        action_url_regex = r"http[^ ]*/auth/password/reset/[^ ]*/"
    elif email_type == "email confirm":
        subject_substring = "Confirm Your E-mail"
        action_url_regex = r"http[^ ]*/auth/email/confirm/[^ ]*/"
    else:
        raise NotImplementedError(f"{email_type}")

    context.test.assertIn(subject_substring, email.subject)

    action_url_search = re.search(action_url_regex, email.body)

    context.test.assertTrue(action_url_search, f"Expected to find link matchin {action_url_regex} in email body: {email.body}")
    context.action_url = action_url_search[0]
    context.action_url_type = email_type


@then(u'the password reset link resets their password')
def step_impl(context: BehaveContext):
    context.test.assertEqual(context.action_url_type, "password reset")
    response = context.test.client.get(context.action_url)
    context.test.assertEqual(response.status_code, 302, "First redirect to password form page")

    password_page_url = response["location"]

    response = context.test.client.get(password_page_url)
    context.test.assertEqual(response.status_code, 200, "Form page load")

    response = context.test.client.post(password_page_url, data={
            "password1": "coco2017",
            "password2": "coco2017"
    })

    context.test.assertRedirects(response, "/auth/password/reset/key/done/")


@then(u'the email confirm link confirms their email')
def step_impl(context: BehaveContext):
    context.test.assertEqual(context.action_url_type, "email confirm")
    response = context.test.client.get(context.action_url)
    context.test.assertRedirects(response, "/profile/")


@then(u'the user is {neg} redirected to {url}')
def step_impl(context: BehaveContext, neg: str, url: str):
    context.test.assertEqual(context.response.status_code, 302, "The user should be redirected")
    if neg == "not":
        context.test.assertNotEqual(context.response.url, url, f"The user should not be redirect to {url}")
    elif neg == "indeed":
        context.test.assertEqual(context.response.url, url, f"The user should be redirect to {url}")
