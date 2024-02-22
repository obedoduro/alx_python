#!/usr/bin/python3

""" Script that uses JSONPlaceholder API to get information about employees and exports data in JSON format """
import requests
import json


def export_all_tasks_to_json():
    url = 'https://jsonplaceholder.typicode.com/'

    users_response = requests.get(url + 'users')
    users = users_response.json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        todos_response = requests.get(url + f'todos?userId={user_id}')
        todos = todos_response.json()

        user_tasks = []
        for todo in todos:
            task_info = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            user_tasks.append(task_info)

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    export_all_tasks_to_json()
