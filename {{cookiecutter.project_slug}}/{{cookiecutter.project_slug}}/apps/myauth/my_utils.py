from django.conf import settings
import requests

url_api = "https://api.mailgun.net/v3/routes"

def create_rule_forward(forward_email=None, from_email=None, description=None, priority=0):
    return {
        "priority": priority,
        "description": description,
        "expression": f"match_recipient('{from_email}')",
        "actions": [f"forward('{forward_email}')", "stop()"]
    }

def create_rule(**kwargs):
    print(kwargs)
    return
    ret = requests.post(url_api, auth=("api", settings.MAILGUN_API_KEY), data=kwargs)
    answer = ret.json()
    print(answer['message'])
    print(answer['route']['id'])

    return answer['route']['id']