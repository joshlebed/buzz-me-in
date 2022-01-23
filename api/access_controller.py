import time

from flask import current_app as app

import buzzer
import utils

hardcoded_access_codes = ["let me in"]


def handle_unlock_request(access_code):
    """decide if access code is valid"""
    if access_code == "":
        return utils.bad_request_response()

    if access_code.lower().strip() in hardcoded_access_codes:
        try:
            response = buzzer.send_buzz(app.config["SWITCHBOT_AUTH"])
            utils.log(response)
            if not response or response.status_code != 200:
                raise Exception("failed to buzz")

            # this is bad programming... maybe do it client side instead
            time.sleep(2)

            return {"success": True, "errorCode": 0, "message": "buzzed"}

        except utils.RequestFailedException:
            return {
                "success": False,
                "errorCode": 3,
                "message": "failed to reach buzzer :(",
            }

        except Exception:
            return {"success": False, "errorCode": 2, "message": "failed to buzz"}

    return {"success": False, "errorCode": 1, "message": "invalid access code"}
