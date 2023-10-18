import requests
import json
import sys

def export_employee_todo_progress(employee_id):
    """
    Export an employee's TODO list progress in JSON format.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
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
