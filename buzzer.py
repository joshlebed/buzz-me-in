"""
docstring
"""

import json
from ratelimit import limits
import sys
import signal
import time
import requests
import argparse

BASE_URL = "https://api.switch-bot.com/"


def get_auth_header(auth_token):
    return {
        "Authorization": auth_token,
    }


def get_config(file_path):
    try:
        with open(file_path) as auth_file:
            config = json.load(auth_file)
            return {"switchbot_auth": config["switchbot_auth"]}
    except:
        return False


def print_response(response):
    print(json.dumps(json.loads(response.text), indent=2))


class SwitchBotAPI(object):
    def __init__(self, switchbot_auth):
        self.switchbot_auth = switchbot_auth

    def get_devices(self):
        get_devices_url = BASE_URL + "v1.0/devices"
        response = requests.get(
            get_devices_url, headers=get_auth_header(self.switchbot_auth)
        )
        print_response(response)

    @limits(calls=1, period=5)
    def send_buzz(self):
        if True:
            print("buzzing")
            return

        buzzer_bot_id = "FEEC403B37A8"
        post_buzz_url = BASE_URL + "v1.0/devices/" + buzzer_bot_id + "/commands"
        body = {"command": "turnOn", "parameter": "default", "commandType": "command"}
        response = requests.post(
            post_buzz_url,
            headers=get_auth_header(self.switchbot_auth),
            json=body,
        )
        print_response(response)
        print("sent")


def main():
    parser = argparse.ArgumentParser(description="buzz the door")
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="path to config.json",
    )
    args = parser.parse_args()
    config_path = args.config
    config = get_config(config_path)
    if not config:
        print("invalid config, exiting")
        return

    switchBotAPI = SwitchBotAPI(config["switchbot_auth"])
    switchBotAPI.send_buzz()
    # switchBotAPI.get_devices()


if __name__ == "__main__":
    main()
