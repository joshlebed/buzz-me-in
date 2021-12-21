# buzz-me-in

twilio -> switchbot service to let you manage access

## notes

you need a `config.json` in the root directory for switchbot auth. example
`config.json` looks like this:

```json
{
  "SWITCHBOT_AUTH": "[auth key here]"
}
```

## dev quickstart

TODO: maybe eventually switch to GCP's
[local dev server](https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app#local-dev-server)

prereqs:

- python3.7+

install venv package globally:

```bash
python3 -m pip install venv
```

set up virtual environment (in root dir):

```bash
python3 -m venv .env      # create virtual env
source .env/bin/activate  # activate virtual env
# install dependencies and test dependencies
pip install -r requirements.txt -r requirements-test.txt -r requirements-dev.txt
deactivate                # deactivate virtual env
```

to run server locally (with virtual environment activated):

```bash
python main.py
```

to run tests:

```bash
pytest
```

NOTE: to run the server, currently you need an authorized google cloud service
account key file on your machine, as well as the
`GOOGLE_APPLICATION_CREDENTIALS` env var set to the location of that file. This
is just for logs. TODO: remove google logs dependency or set logs to only use
google when on the server

## deployment stuff

Currently, this app is deployed and hosted with Google Cloud Platform.
`app.yaml` and `.gcloudignore` are config files for the `gcloud` which is used
to deploy this app to GCP.

prereqs for deployment:

- your google account must be given privileges
- download their `gcloud` \([docs](https://cloud.google.com/sdk/gcloud)\) CLI
  tool [here](https://cloud.google.com/sdk/docs/quickstart).

to deploy a new version (from root dir):

```bash
gcloud app deploy
```
