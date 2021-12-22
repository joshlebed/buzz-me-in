"""tests for main.py"""

import main


def test_index():
    """test root path GET"""

    main.app.testing = True
    client = main.app.test_client()

    response = client.get("/")
    assert response.status_code == 200


# TODO: mock the api call, mock the webhook call
def test_sms_success():
    """test SMS webhook"""

    return

    main.app.testing = True
    client = main.app.test_client()

    response = client.post("/test/", data={"body": "aaa"})
    print(response)
    assert response.status_code == 200
