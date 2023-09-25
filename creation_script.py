import json

from csv import DictReader

from input_files import BOOKS
from input_files import USERS


result_json = []


def read_books(file):
    with open(file, newline='') as f:
        reader = DictReader(f)
        for row in reader:
            row.pop("Publisher")
            yield row


with open(USERS, "r") as f:
    users = json.loads(f.read())
    for user in users:
        user_dict = {}
        user_dict.update(
            {"name": user["name"],
             "gender": user["gender"],
             "address": user["address"],
             "age": user["age"],
             "books": []
             })
        result_json.append(user_dict)

one_book = read_books(BOOKS)

while True:
    try:
        for item in result_json:
            item["books"].append(next(one_book))
    except StopIteration:
        break

with open('result.json', "w") as f:
    s = json.dumps(result_json, indent=4)
    f.write(s)
