#!/usr/bin/python3
"""
Retrieve employee TODO list information using a REST API and export to CSV
"""

import requests
import csv
from sys import argv

def get_employee_todo(employee_id):
    """
    Retrieve employee TODO list information and export to CSV

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None
    """
    # Fetching employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data:
        print(f"No employee found with ID: {employee_id}")
        exit(1)

    employee_name = user_data.get("name")

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            csv_writer.writerow([employee_id, employee_name, str(task["completed"]), task["title"]])

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    get_employee_todo(employee_id)
