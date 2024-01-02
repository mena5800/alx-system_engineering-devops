#!/usr/bin/python3
"""3. Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url_employee = 'https://jsonplaceholder.typicode.com/users'
    # .jons() convert json object to dict
    response_employees = requests.get(url_employee).json()

    obj_to_save = {}
    for employee in response_employees:
        username = employee.get("username")
        id = employee.get("id")
        tasks = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)
        response_tasks = requests.get(tasks).json()
        obj_to_save[id] = []
        for task in response_tasks:
            obj_to_save[id].append({"username": username, "task": task.get(
                "title"), "completed": task.get("completed")})

    with open("todo_all_employees.json", "w", newline="") as f:
        json.dump(obj_to_save, f)
