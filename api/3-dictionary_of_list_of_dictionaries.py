#!/usr/bin/python3
"""
This script fetches user and task data from a public
API and writes it to a JSON file.
"""

import json
import requests


def fetch_data():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    return users, todos


def main():
    users, todos = fetch_data()
    data = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_tasks = [task for task in todos if task["userId"] == user_id]
        data[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in user_tasks
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
