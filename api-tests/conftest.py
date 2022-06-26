import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="Get url from CLI")
    parser.addoption("--status_code", action="store", default=200, help="Get status_code from CLI")


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--url"), request.config.getoption("--status_code")
