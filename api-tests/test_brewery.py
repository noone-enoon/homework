import pytest
import requests
from jsonschema import validate, ValidationError

states = ["West Virginia", "California", "Florida"]
types = ["micro", "nano", "regional", "brewpub", "large", "planning"]
schema = {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "brewery_type": {"type": "string"},
    "street": {"type": "string"},
    "address_2": {"type": type(None)},
    "address_3": {"type": type(None)},
    "city": {"type": "string"},
    "state": {"type": "string"},
    "county_province": {"type": type(None)},
    "postal_code": {"type": "string"},
    "country": {"type": "string"},
    "longitude": {"type": "string"},
    "latitude": {"type": "string"},
    "phone": {"type": "string"},
    "website_url": {"type": "string"},
    "updated_at": {"type": "string"},
    "created_at": {"type": "string"}
}


def test_get_random_brewery():
    """рандомная пивоварня равна пиповарне, отфильтрованной по имени из всего списка пивоварен,
    можно его параметризовать"""
    random_brewery = requests.get("https://api.openbrewerydb.org/breweries/random")
    assert random_brewery.ok is True

    name_random_brewery = random_brewery.json()[0]["name"]

    all_breweries_filtered_by_name = requests.get("https://api.openbrewerydb.org/breweries",
                                                  params={"by_name": name_random_brewery})
    assert all_breweries_filtered_by_name.ok is True

    assert random_brewery.json()[0] == all_breweries_filtered_by_name.json()[0]


def test_get_single_brewery():
    """получить список всех пивоварен и по имени из него получить одну единственную пивоварню"""
    all_breweries = requests.get("https://api.openbrewerydb.org/breweries")
    assert all_breweries.ok is True

    id_brewery = all_breweries.json()[0]["id"]

    single_breweries = requests.get(f"https://api.openbrewerydb.org/breweries/{id_brewery}")
    assert single_breweries.ok is True

    assert single_breweries.json() in all_breweries.json()


@pytest.mark.parametrize("state", states)
def test_filter_breweries_by_state(state):
    filtered_breweries_by_state = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    assert filtered_breweries_by_state.ok is True

    for brewery in filtered_breweries_by_state.json():
        assert brewery["state"] == state


@pytest.mark.parametrize("type", types)
def test_filter_breweries_by_type(type):
    filtered_breweries_by_type = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={type}")
    assert filtered_breweries_by_type.ok is True

    for brewery in filtered_breweries_by_type.json():
        assert brewery["brewery_type"] == type


def test_check_json_schema():
    single_brewery = requests.get("https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati")
    assert single_brewery.ok is True
    try:
        validate(instance=single_brewery.json(), schema=schema)
    except ValidationError:
        return 1
