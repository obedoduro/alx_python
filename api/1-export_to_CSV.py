import requests
import csv
import sys

def export_employee_todo_progress(employee_id):
    """
    Export an employee's TODO list progress in CSV format.

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

    # Create a CSV file for the employee's TODO list
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the TODO list data to the CSV file
        for task in todo_data:
            task_completed_status = "True" if task.get("completed") else "False"
            csv_writer.writerow([user_id, username, task_completed_status, task.get("title")])

    print(f"Data has been exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
