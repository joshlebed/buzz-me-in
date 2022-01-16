"""this is the entrypoint to the Flask app. it handles routing"""

import json

import google.cloud.logging
from flask import Flask, Response, request

import access_controller
import buzzer
import sms_handler
import utils

app = Flask(__name__, static_folder="../build/", static_url_path="/")
app.config.from_file("config.json", load=json.load)

client = google.cloud.logging.Client()
client.setup_logging()


@app.route("/api/sms", methods=["POST"])
def handle_sms():
    """handle sms webhook from twilio"""
    utils.log("hit /api/sms/")
    return sms_handler.handle_sms(request)


@app.route("/api/unlock/<access_code>")
def handle_api_unlock(access_code=""):
    """handle buzz request from frontend"""
    utils.log("hit /api/unlock/<access_code>")
    utils.log(access_code)
    return access_controller.handle_unlock_request(access_code)


# catch all other paths
# @app.route("/")
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handle_all_other_urls(path):
    """render react app"""
    utils.log(f"rendering app with path: {path}")
    return app.send_static_file("index.html")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="localhost", port=8080, debug=True)
