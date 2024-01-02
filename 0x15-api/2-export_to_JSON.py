#!/usr/bin/python3
"""2. Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url_employee = 'https://jsonplaceholder.typicode.com/users?id={}'.format(
        id)
    url_tasks = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    # .jons() convert json object to dict
    response_employee = requests.get(url_employee).json()
    username = response_employee[0].get("username")

    response_tasks = requests.get(url_tasks).json()

    obj_to_save = {id: []}
    for task in response_tasks:
        obj_to_save[id].append({"task": task.get(
            "title"), "completed": task.get("completed"),
            "username": username})

    with open("{}.json".format(id), "w", newline="") as f:
        json.dump(obj_to_save, f)
