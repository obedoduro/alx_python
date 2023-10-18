import requests
import sys

def get_employee_info(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to get employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()

    # Send a GET request to get the TODO list for the employee
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Print employee's TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Print titles of completed tasks
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
