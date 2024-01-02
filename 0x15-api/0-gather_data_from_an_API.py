#!/usr/bin/python3
"""0. Gather data from an API"""
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
    name = response_employee[0]["name"]

    response_tasks = requests.get(url_tasks).json()
    completed_tasks = []

    for task in response_tasks:
        if task["completed"] is True:
            completed_tasks.append(task["title"])

    print("Employee {} is done with tasks({}/{}):".format(name,
          len(completed_tasks), len(response_tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))
