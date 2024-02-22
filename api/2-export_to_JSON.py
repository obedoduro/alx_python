import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py USER_ID")
        exit(1)

    user_id = argv[1]

    try:
        request_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id))
        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id))

        if request_employee.status_code != 200 or request_todos.status_code != 200:
            print("Failed to retrieve data. Please verify the USER_ID.")
            exit(1)

        user = json.loads(request_employee.text)
        username = user.get("username")
        user_todos = json.loads(request_todos.text)

        tasks = []

        for todo in user_todos:
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            tasks.append(task)

        with open('{}.json'.format(user_id), 'w') as json_file:
            json.dump({user_id: tasks}, json_file)

        print("Correct USER_ID: OK")

    except Exception as e:
        print("An error occurred:", e)
