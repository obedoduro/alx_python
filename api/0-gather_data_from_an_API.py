import requests
import sys

def get_employee_info(employee_id):
    """
    Retrieve and display employee's TODO list progress.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()

    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
