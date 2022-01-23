"""some functions for handling sms response business logic"""

from flask import current_app as app
from twilio.twiml.messaging_response import MessagingResponse

import buzzer
import utils


def handle_sms(request):
    """handle incoming sms and respond"""
    utils.log(request)
    if request.method == "POST":
        body = request.values.get("Body", None)
        if not body:
            return unauthorized_texter_response()

        return handle_message_body(body)

    return utils.bad_request_response()


def handle_message_body(body):
    """respond to SMS message body with SMS response"""
    utils.log("handling message: " + body)
    resp = MessagingResponse()
    if body.lower().strip() == "let me in":
        try:
            response = buzzer.send_buzz(app.config["SWITCHBOT_AUTH"])
            utils.log(response)
            if not response or response.status_code != 200:
                raise utils.RequestFailedException("failed to buzz")

            resp.message("welcome!")

        except utils.RequestFailedException:
            resp.message("failed to reach buzzer :(")

        except Exception:
            resp.message("unknown error :(")

    else:
        resp.message("unauthorized")

    return str(resp)


def unauthorized_texter_response():
    resp = MessagingResponse()
    resp.message("no passcode detected")
    return str(resp)
