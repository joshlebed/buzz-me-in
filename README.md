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
python api/main.py
```

to run server in Google's dev server locally to mimic the prod environment:

```bash
dev_appserver.py --env_var GOOGLE_APPLICATION_CREDENTIALS=[path to your credentials] .
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
yarn build          # build the react app
gcloud app deploy   # push to prod server
```

---

# Create React App readme

This project was bootstrapped with
[Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests)
for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best
performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about
[deployment](https://facebook.github.io/create-react-app/docs/deployment) for
more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can
`eject` at any time. This command will remove the single build dependency from
your project.

Instead, it will copy all the configuration files and the transitive
dependencies (webpack, Babel, ESLint, etc) right into your project so you have
full control over them. All of the commands except `eject` will still work, but
they will point to the copied scripts so you can tweak them. At this point
you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for
small and middle deployments, and you shouldn't feel obligated to use this
feature. However we understand that this tool wouldn't be useful if you couldn't
customize it when you are ready for it.

## Learn More

You can learn more in the
[Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here:
[https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here:
[https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here:
[https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here:
[https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here:
[https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here:
[https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
