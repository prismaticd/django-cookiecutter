from django.test import TestCase
from django.urls import reverse


class ViewTest(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse("core_app:home-page"))

        self.assertEqual(response.status_code, 200)
