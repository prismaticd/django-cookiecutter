from django.test import TestCase
from . import factories
from allauth.account.models import EmailAddress


class FactoryTest(TestCase):

    """
    Sanity checks for the factories
    """

    def assertUserFactory(self, user_factory):
        user = user_factory()

        self.assertIn("@", user.email)
        self.assertTrue(user.username)

        emails = user.emailaddress_set.all()

        self.assertEqual(len(emails), 1)

        main_email = emails[0]

        self.assertEqual(main_email.email, user.email)
        self.assertTrue(main_email.primary)

        self.assertEqual(list(emails), list(EmailAddress.objects.filter(user=user)))

        return user

    def test_user_factory(self):
        user = self.assertUserFactory(factories.UserFactory)

        main_email = user.emailaddress_set.all()[0]
        self.assertFalse(main_email.verified)

    def test_verified_user_factory(self):
        user = self.assertUserFactory(factories.VerifiedUserFactory)

        main_email = user.emailaddress_set.all()[0]
        self.assertTrue(main_email.verified)
