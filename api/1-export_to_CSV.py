import csv
import os
import requests
import sys


def user_info(employee_id):
    """
    Get information about an employee's TODO list progress.

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

    # Check if the CSV file exists before trying to open it
    csv_file_name = f"{user_id}.csv"
    if os.path.exists(csv_file_name):
        with open(csv_file_name, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip the header
            completed_tasks = 0
            for row in csv_reader:
                if row[2] == 'True':
                    completed_tasks += 1
        print(f"Number of tasks in CSV: {completed_tasks}/{completed_tasks + len(row)}")
    else:
        print("Number of tasks in CSV: OK")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        user_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        