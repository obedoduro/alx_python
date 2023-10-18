import json
import requests


def export_all_employee_todo_progress():
    base_url = "https://jsonplaceholder.typicode.com"

    # Get a list of all employees
    employees_response = requests.get(f"{base_url}/users")
    employees_data = employees_response.json()

    # Initialize an empty dictionary to store the data
    all_todo_data = {}

    for employee in employees_data:
        employee_id = str(employee.get("id"))
        username = employee.get("username")

        # Get employee's TODO list
        todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        todo_data = todo_response.json()

        # Prepare data for the employee
        employee_todo_list = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todo_data
        ]

        # Add the employee's data to the dictionary
        all_todo_data[employee_id] = employee_todo_list

    # Write the data to the JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_todo_data, json_file, indent=4)

    print("Data has been exported to todo_all_employees.json")

if __name__ == "__main__":
    export_all_employee_todo_progress()
