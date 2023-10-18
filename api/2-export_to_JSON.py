"""
Export an employee's TODO list progress in JSON format.

This script retrieves an employee's TODO list from a REST API and exports it in JSON format. The JSON data is structured as { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ] }.

Usage:
    python script.py <employee_id>
"""


import json
import requests
import sys


def export_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Create a JSON structure for the employee's TODO list
    todo_list = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todo_data
        ]
    }

    # Write the JSON data to a file
    json_file_name = f"{user_id}.json"
    with open(json_file_name, "w") as json_file:
        json.dump(todo_list, json_file, indent=4)

    # Check if the JSON file has the correct USER_ID
    with open(json_file_name, "r") as json_file:
        data = json.load(json_file)
        if user_id == list(data.keys())[0]:
            print("Correct USER_ID: OK")
        else:
            print("Correct USER_ID: NOT OK")

    print(f"Data has been exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        