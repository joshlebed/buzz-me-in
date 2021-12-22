"""some functions for handling sms response business logic"""

from flask import current_app as app
from twilio.twiml.messaging_response import MessagingResponse

import buzzer
import utils


def handle_message_body(body):
    """handle incoming sms and respond"""
    utils.log("handling message: " + body)
    resp = MessagingResponse()
    if body.lower().strip() == "let me in":
        try:
            response = buzzer.send_buzz(app.config["SWITCHBOT_AUTH"])
            utils.log(response)
            if not response or response.status_code != 200:
                raise Exception("failed to buzz")

            resp.message("welcome!")

        except:
            resp.message("failed :(")

    else:
        resp.message("unauthorized")

    return str(resp)


def unauthorized_texter_response():
    resp = MessagingResponse()
    resp.message("no passcode detected")
    return str(resp)
