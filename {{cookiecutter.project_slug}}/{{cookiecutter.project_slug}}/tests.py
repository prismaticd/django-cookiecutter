from django.test.testcases import TestCase
from django.core.management import call_command
import json


class {{ cookiecutter.project_name|replace(" ", "") }}Test(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     call_command('init_data')

    def test_health(self):
        res = self.client.get('/healthcheck/')
        self.assertEqual(res.status_code, 200)
        response = json.loads(res.content)
        self.assertEqual(response.get('db'), 'ok')