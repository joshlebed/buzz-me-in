from flask import current_app as app

import buzzer
import utils


def handle_unlock_request(access_code):
    """decide if access code is valid"""
    if access_code == "":
        return utils.bad_request_response()

    if access_code.lower().strip() == "1":
        try:
            response = buzzer.send_buzz(app.config["SWITCHBOT_AUTH"])
            utils.log(response)
            if not response or response.status_code != 200:
                raise Exception("failed to buzz")

            return {"success": True, "message": "buzzed"}

        except utils.RequestFailedException:
            return {"success": False, "message": "failed to reach buzzer :("}

        except Exception:
            return {"success": False, "message": "failed to buzz"}

    return {"success": False, "message": "invalid access code"}
