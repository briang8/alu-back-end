#!/usr/bin/python3
"""
This script exports an employee's todo list progress to a CSV file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")
    tasks = []

    for todo in todos_data:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username,
        }
        tasks.append(task)

    data = {user_id: tasks}

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file)
