import pytest
import requests

titles = ['test_1', 'test_2', 'test_3']
user_ids = [1, 2, 3]
schema = {
    'userId': {'type': 'integer'},
    'id': {'type': 'integer'},
    'title': {'type': 'object'},
    'body': {'type': 'object'}
}


@pytest.mark.parametrize("title", titles)
def test_create_resource(title):
    body = {"title": title, "body": "test", "userId": 1}
    response = requests.post(url="https://jsonplaceholder.typicode.com/posts",
                             headers={"Content-type": "application/json; charset=UTF-8"},
                             json=body)
    assert response.ok is True

    response_body = {k: v for k, v in response.json().items() if k != "id"}
    assert response_body == body


def test_upload_resource():
    update_response = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                                   data={"id": 1, "title": "my", "body": "my_body", "userId": 1})
    assert update_response.ok is True
    assert update_response.json() == {"id": 1, "title": "my", "body": "my_body", "userId": '1'}


def test_delete_resource():
    delete_resource = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert delete_resource.ok is True


@pytest.mark.parametrize("id", user_ids)
def test_filter(id):
    filtered_resource = requests.get(url=f"https://jsonplaceholder.typicode.com/posts?userId={id}")
    assert filtered_resource.ok is True

    for item in filtered_resource.json():
        assert item["userId"] == id


def test_patch_resources():
    response = requests.patch(url="https://jsonplaceholder.typicode.com/posts/1", json={"title": "my_test"})
    assert response.ok is True

    assert response.json()["title"] == "my_test"
