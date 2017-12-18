from unittest import skip

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from requests.models import Response

from {{ cookiecutter.project_slug }}.apps.profile.models import Profile


def my_side_effect_profile(user, profile, *args, **kwargs):
    response = Response()
    response.status_code = 200
    response._content['message'] = "Route has been created"
    return response


@skip
class MyAuthTest(TestCase):

    def test_registration_first_step(self):
        ret = self.client.post("/auth/register/", data={"email": "test@test.com",
                                                    "password1": "coco2017",
                                                    "password2": "coco2017"})
        self.assertEqual(ret.status_code, 302, "The registration did not redirect")
        self.assertEqual(ret.url, "/profile/", "Wrong redirection when creating new account")
        user = User.objects.all().filter(email="test@test.com").first()
        self.assertIsNotNone(user, 'The user has not been created')
        self.assertIsNotNone(Profile.objects.filter(user=user), 'The Profile has not been created')

    def test_registration_complete(self):
        ret = self.client.post("/auth/register/", data={"email": "test@email.com",
                                                        "password1": "coco2017",
                                                        "password2": "coco2017"})
        self.assertEqual(ret.url, "/profile/", "Wrong redirection when creating new account")
        data_formset = {"user_formset-TOTAL_FORMS": 1, "user_formset-INITIAL_FORMS": 1,
                        "user_formset-MIN_NUM_FORMS": 1000, "user_formset-MAX_NUM_FORMS": 0,
                        "user_formset-0-last_name": "lastTest", "user_formset-0-first_name": "firstTest",
                        "user_formset-0-id": ret.context['user'].id, "profile_formset-0-id": ret.context['user'].id,
                        "profile_formset-TOTAL_FORMS": 1, "profile_formset-INITIAL_FORMS": 1,
                        "profile_formset-MIN_NUM_FORMS": 1000, "profile_formset-MAX_NUM_FORMS": 0,
                        "profile_formset-0-forward_email_1": ret.context['user'].email,
                        "profile_formset-0-forward_email_2": ret.context['user'].email,
                        "profile_formset-0-forward_email_3": ""
                        }
        self.client.post("/profile/", data=data_formset)
