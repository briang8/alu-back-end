#!/usr/bin/python3
"""
This script gathers data from an API and displays
the completed tasks of an employee.
"""
import sys
import requests

def fetch_employee_data(employee_id):
    # The base URL for the API endpoint
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    # Sending GET request to the API
    response = requests.get(url)
    
    # If the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        sys.exit(1)

def display_progress(employee_id, tasks):
    # Filter completed tasks
    completed_tasks = [task for task in tasks if task['completed']]
    
    # Get employee's name from another endpoint (users)
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        employee_name = user_response.json()['name']
    else:
        print(f"Failed to retrieve data for employee name {employee_id}")
        sys.exit(1)

    # Display the progress
    total_tasks = len(tasks)
    completed_count = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    
    # Display completed tasks
    for task in completed_tasks:
        print(f"     {task['title']}")

def main():
    # Accept employee ID from command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    tasks = fetch_employee_data(employee_id)
    display_progress(employee_id, tasks)

if __name__ == "__main__":
    main()