from django.test.testcases import TestCase

from .factories import UserFactory
from ..templatetags.myauth_tags import get_user_primary_email, get_user_other_emails


class TemplateTagsTest(TestCase):

    def setUp(self):

        self.user = UserFactory(extra_emails=2)
        UserFactory.create_batch(size=3, extra_emails=2)

    def test_get_user_primary_email(self):
        email = get_user_primary_email(self.user)

        self.assertEqual(email.user, self.user)
        self.assertTrue(email.primary)

    def test_get_user_other_emails(self):
        other_emails = get_user_other_emails(self.user)

        self.assertEqual(len(other_emails), 2)
        for e in other_emails:
            self.assertEqual(e.user, self.user)
            self.assertFalse(e.primary)
