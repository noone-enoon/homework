import requests
import pytest

breed_dogs = ["groenendael", "keeshond", "leonberg"]


@pytest.mark.parametrize("breed", breed_dogs)
def test_get_breed_images(breed):
    images = requests.get(f"https://dog.ceo/api/breed/{breed}/images")
    assert images.ok is True

    images_iter = (image for image in images.json()["message"])

    for image in images_iter:
        assert breed in image


@pytest.mark.parametrize("breed", breed_dogs)
def test_get_image_for_breed(breed):
    image = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    all_images_for_breed = requests.get(f"https://dog.ceo/api/breed/{breed}/images")

    assert image.ok is True
    assert all_images_for_breed.ok is True

    assert image.json()["message"] in all_images_for_breed.json()["message"]


def test_get_sub_breeds():
    sub_breeds = requests.get("https://dog.ceo/api/breed/hound/list")
    all_breeds = requests.get("https://dog.ceo/api/breeds/list/all")

    assert sub_breeds.ok is True
    assert all_breeds.ok is True

    assert sub_breeds.json()["message"] == all_breeds.json()["message"]["hound"]


def test_get_random_image_breed_in_name():
    random_image = requests.get("https://dog.ceo/api/breeds/image/random")
    assert random_image.ok is True

    random_image_mass = random_image.json()["message"].split("/")
    breed_sub_breed = random_image_mass[4].split("-")

    all_breeds = requests.get("https://dog.ceo/api/breeds/list/all")
    assert all_breeds.ok is True

    assert breed_sub_breed[0] in all_breeds.json()["message"]


def test_get_random_image_sub_breed_in_name():
    random_image = requests.get("https://dog.ceo/api/breeds/image/random")
    assert random_image.ok is True

    random_image_mass = random_image.json()["message"].split("/")
    breed_sub_breed = random_image_mass[4].split("-")

    all_breeds = requests.get("https://dog.ceo/api/breeds/list/all")
    assert all_breeds.ok is True

    for breed, sub_breed in all_breeds.json()["message"].items():
        if breed_sub_breed[0] == breed:
            assert breed_sub_breed[1] in sub_breed
