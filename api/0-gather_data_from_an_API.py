#!/usr/bin/python3
"""
This script gathers data from an API and displays
the completed tasks of an employee.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Get employee data
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    employee_name = user.get("name")

    # Get employee's todo list
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))