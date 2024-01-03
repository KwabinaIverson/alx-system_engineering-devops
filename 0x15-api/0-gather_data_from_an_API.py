#!/usr/bin/python3
"""
Retrieve employee TODO list information using a REST API
"""

import requests
from sys import argv

def get_employee_todo(employee_id):
    """
    Retrieve employee TODO list information

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

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks})")

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    get_employee_todo(employee_id)
