"""fetching employee,TODO lists and counting completed tasks
"""

import requests
import json


def export_tasks_to_json(user_id):
    """
    Export tasks owned by a specific user to a JSON file.

    Args:
        user_id (int): The ID of the user whose tasks need to be exported.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': user_id}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        tasks = response.json()
        user_tasks = []

        for task in tasks:
            user_tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": task['username']
            })

        filename = f"{user_id}.json"
        with open(filename, 'w') as json_file:
            json.dump({user_id: user_tasks}, json_file, indent=4)

        print(f"Tasks exported to {filename} successfully.")
    else:
        print(
            f"Failed to retrieve tasks for user {user_id}. Status code: {response.status_code}")


if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    export_tasks_to_json(user_id)
