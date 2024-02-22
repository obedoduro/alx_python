"""fetching employee,TODO lists and counting completed tasks
"""

import csv
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    # Get employee details
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = response.json()['name']

    # Get employee TODO list
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])

    
    for todo in todos:
        if todo['completed']:
            print(f'\t{todo["title"]}')

    # Export data to CSV file
    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                            todo['completed'], todo['title']])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_list_progress(employee_id)
