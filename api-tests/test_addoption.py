import requests


def test_check_status_code(cmdopt):
    response = requests.get(url=cmdopt[0])

    assert response.status_code == cmdopt[1]
