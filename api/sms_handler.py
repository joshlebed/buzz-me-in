"""some functions for handling sms response business logic"""

from flask import current_app as app
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

import buzzer
import sms_handler
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
            sms_handler.notify_admins(
                f"someone just buzzed via SMS with the code: {body}"
            )
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
        sms_handler.notify_admins(
            f"someone just failed to buzz via SMS with the code: {body}"
        )

        resp.message("unauthorized")

    return str(resp)


def unauthorized_texter_response():
    resp = MessagingResponse()
    resp.message("no passcode detected")
    return str(resp)


def notify_admins(message_body):
    # TODO: get admins phone numbers from DB
    admin_phone_numbers = ["+12404542471", "+14109922852"]
    for admin_phone_number in admin_phone_numbers:
        account_sid = app.config["TWILIO_ACCOUNT_SID"]
        auth_token = app.config["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
                body=message_body, from_="+16076008223", to=admin_phone_number
            )
        except Exception as e:
            print("failed to notify admins")
            print(e)

        print(message.sid)
