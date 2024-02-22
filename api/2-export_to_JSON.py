#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""
import json
import requests
from sys import argv


def export_tasks_to_json(user_id, tasks):
    data = {user_id: []}
    for task in tasks:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_info.get("username")
        }
        data[user_id].append(task_info)

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1] if len(sys.argv) > 1 else None

    if user_id is None:
        print("Please provide a user ID as a command-line argument.")
        sys.exit(1)

    user_endpoint = f"{url}users/{user_id}"
    todos_endpoint = f"{url}todos?userId={user_id}"

    user_res = requests.get(user_endpoint)
    if user_res.status_code != 200:
        print(f"Failed to retrieve user data for user ID {user_id}.")
        sys.exit(1)

    user_info = user_res.json()

    print(f"Employee {user_info.get('name')} is done with tasks", end="")

    tasks_res = requests.get(todos_endpoint)
    if tasks_res.status_code != 200:
        print(f"Failed to retrieve tasks data for user ID {user_id}.")
        sys.exit(1)

    tasks = tasks_res.json()
    completed_tasks = [task for task in tasks if task.get("completed")]

    print(f" ({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")

    export_tasks_to_json(user_id, tasks)
