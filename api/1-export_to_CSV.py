#!/usr/bin/python3
"""
This script exports an employee's todo list progress to a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks data
    tasks_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Write to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            writer.writerow(
                [
                    employee_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ]
            )
            