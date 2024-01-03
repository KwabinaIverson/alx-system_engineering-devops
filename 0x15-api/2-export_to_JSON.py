#!/usr/bin/python3
"""
Retrieve employee TODO list information using a REST API and export to JSON
"""

import requests
import json
from sys import argv

def get_employee_todo(employee_id):
    """
    Retrieve employee TODO list information and export to JSON

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

    json_file_name = f"{employee_id}.json"

    result = {str(employee_id): [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in todos_data]}

    with open(json_file_name, 'w') as json_file:
        json.dump(result, json_file, indent=2)

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    get_employee_todo(employee_id)
