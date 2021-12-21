"""
docstring
"""


import json
import argparse
import requests
from ratelimit import limits
import utils


BASE_URL = "https://api.switch-bot.com/"


def print_response(response):
    print(json.dumps(json.loads(response.text), indent=2))


@limits(calls=1, period=5)
def send_buzz(switchbot_auth):
    utils.log("buzzing")
    buzzer_bot_id = "FEEC403B37A8"
    post_buzz_url = BASE_URL + "v1.0/devices/" + buzzer_bot_id + "/commands"
    body = {"command": "turnOn", "parameter": "default", "commandType": "command"}
    return requests.post(
        post_buzz_url,
        headers=utils.get_auth_header(switchbot_auth),
        json=body,
    )
