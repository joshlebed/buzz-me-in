import json
import logging

import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()


def log(msg):
    print("info: " + str(msg))
    logging.info(msg)


def get_auth_header(auth_token):
    return {
        "Authorization": auth_token,
    }


def get_config(file_path):
    try:
        with open(file_path, "r") as auth_file:
            config = json.load(auth_file)
            return {"switchbot_auth": config["switchbot_auth"]}

    except:
        return False
