"""this is the entrypoint to the Flask app. it handles routing"""

import json

import google.cloud.logging
from flask import Flask, Response, render_template, request

import sms_handler
import utils

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

client = google.cloud.logging.Client()
client.setup_logging()


@app.route("/")
def root():
    """render root page"""
    utils.log("hit main page")
    return render_template("index.html")


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
    app.run(host="127.0.0.1", port=8080, debug=True)
