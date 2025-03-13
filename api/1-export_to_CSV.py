#!/usr/bin/python3
"""
This script exports an employee's todo list progress to a CSV file.
"""
import sys
import requests
import csv

def fetch_employee_data(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        sys.exit(1)

def fetch_employee_name(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        return user_response.json()['name']
    else:
        print(f"Failed to retrieve data for employee name {employee_id}")
        sys.exit(1)

def export_to_csv(employee_id, tasks, employee_name):
    # Define the CSV file name
    csv_filename = f"{employee_id}.csv"
    
    # Open CSV file in write mode
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write each task's data
        for task in tasks:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    tasks = fetch_employee_data(employee_id)
    employee_name = fetch_employee_name(employee_id)
    
    export_to_csv(employee_id, tasks, employee_name)
    print(f"Data exported to {employee_id}.csv")

if __name__ == "__main__":
    main()