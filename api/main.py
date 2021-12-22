"""this is the entrypoint to the Flask app. it handles routing"""

import json

import google.cloud.logging
from flask import Flask, Response, request

import buzzer
import sms_handler
import utils

app = Flask(__name__, static_folder='../build/', static_url_path="/")
app.config.from_file("config.json", load=json.load)

client = google.cloud.logging.Client()
client.setup_logging()


@app.route("/")
def index():
    """render root page"""
    utils.log("hit main page")
    # return render_template("index.html")
    return app.send_static_file('index.html')


@app.route("/sms/", methods=["POST"])
def sms_request():
    """handle sms webhook from twilio"""
    utils.log("hit /sms/")
    if request.method == "POST":
        body = request.values.get("Body", None)
        if not body:
            return sms_handler.unauthorized_texter_response()

        return sms_handler.handle_message_body(body)

    return bad_request_response()


@app.route("/api/unlock/<access_code>")
def buzz_request(access_code=""):
    """handle buzz request from frontend"""
    utils.log("hit /api/<access_code>")
    utils.log(access_code)
    if access_code == "":
        return bad_request_response()

    if access_code.lower().strip() == "1":
        try:
            response = buzzer.send_buzz(app.config["SWITCHBOT_AUTH"])
            utils.log(response)
            if not response or response.status_code != 200:
                raise Exception("failed to buzz")

            return {"success": True, "message": "buzzed"}

        except:
            return {"success": False, "message": "failed to buzz"}

    return {"success": False, "message": "invalid access code"}


def bad_request_response():
    """return 400: bad request"""
    return Response("bad request", status=400)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="0.0.0.0", port=8080, debug=True)
