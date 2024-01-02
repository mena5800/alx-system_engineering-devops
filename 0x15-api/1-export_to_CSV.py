#!/usr/bin/python3
"""1. Export to CSV"""
import csv
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
    completed_tasks = []

    for task in response_tasks:
        completed_tasks.append(task)

    with open("{}.csv".format(id), "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for task in completed_tasks:
            writer.writerow({"USER_ID": id, "USERNAME": username,
                            "TASK_COMPLETED_STATUS": task.get("completed"),
                             "TASK_TITLE": task.get("title")})
