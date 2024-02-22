#!/usr/bin/env python3
"""
1-export_to_CSV.py
Module to gather data from a REST API about an employee's TODO list progress
and export it to a CSV file.
"""

import sys
import requests
import csv


def get_employee_todo_progress(employee_id):
    """
    Function to retrieve and display employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of dictionaries containing task details.
    """
    # URLs for employee details and their TODO list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetching data from the API
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        # Handling response status
        if user_response.status_code != 200:
            print("Error: Unable to fetch employee details.")
            return []
        if todo_response.status_code != 200:
            print("Error: Unable to fetch employee TODO list.")
            return []

        # Parsing JSON responses
        user_data = user_response.json()
        todo_data = todo_response.json()

        # Constructing list of task dictionaries
        tasks = []
        for task in todo_data:
            task_dict = {
                "USER_ID": user_data['id'],
                "USERNAME": user_data['username'],
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            }
            tasks.append(task_dict)

        return tasks

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def export_to_csv(employee_id, tasks):
    """
    Function to export task data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        tasks (list): List of dictionaries containing task details.

    Returns:
        None
    """
    if not tasks:
        print("No tasks found.")
        return

    filename = f"{employee_id}.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writeheader()
            writer.writerows(tasks)
        print(f"Task data exported to {filename}")
    except Exception as e:
        print(f"An error occurred while exporting to CSV: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        tasks = get_employee_todo_progress(employee_id)
        export_to_csv(employee_id, tasks)
