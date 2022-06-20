import json
from csv import DictReader


def get_books_from_csv(path='./books.csv'):
    with open(path, 'r') as file_books:
        reader = DictReader(file_books)
        for row in reader:
            yield row


def get_users_from_json(path='./users.json'):
    with open(path, 'r') as file_users:
        reader = json.load(file_users)
        return (row for row in reader)


def get_custom_structure():
    users_iter = get_users_from_json()
    books_iter = get_books_from_csv()
    result = []

    for user in users_iter:
        result.append({"name": user["name"],
                       "gender": user["gender"],
                       "address": user["address"],
                       "age": user["age"],
                       "books": []})

    result_tmp_iter = (x for x in result)

    for book in books_iter:
        books = []
        books.append({"title": book["Title"],
                      "author": book["Author"],
                      "pages": book["Pages"],
                      "genre": book["Genre"]})

        flag = 0
        for user in result_tmp_iter:
            user['books'].append(books)
            flag = 1
            break

        if flag == 0:
            result_tmp_iter = (x for x in result)

    return result


def write_custom_structure_to_file(data):
    with open('result.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


write_custom_structure_to_file(get_custom_structure())
