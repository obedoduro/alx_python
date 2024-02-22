"""fetching employee,TODO lists and counting completed tasks
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Check if the correct number of arguments is provided """
    if len(argv) != 2:
        print("Usage: python script.py USER_ID")
        exit(1)

    user_id = argv[1]

    try:
        """ Send a GET request to retrieve user information """
        request_employee = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/')

        """ Send a GET request to retrieve the user's to-do list """
        request_todos = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

        """ Check if the HTTP requests were successful """
        if request_employee.status_code != 200 or request_todos.status_code != 200:
            print("Failed to retrieve data. Please verify the USER_ID.")
            exit(1)

        """ Convert the JSON response containing user information into a dictionary """
        user = json.loads(request_employee.text)
        username = user.get("username")

        """ Convert the JSON response containing the to-do list into a list of dictionaries """
        user_todos = json.loads(request_todos.text)

        tasks = []

        """ Iterate through the list of dictionaries representing to-do items """
        for todo in user_todos:
            """ Construct a dictionary representing each task """
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            tasks.append(task)

        """ Write the tasks to a JSON file named USER_ID.json """
        with open(f'{user_id}.json', 'w') as json_file:
            json.dump({user_id: tasks}, json_file)

        """ Print the expected output message """
        print("Correct USER_ID: OK")

    except Exception as e:
        """ Handle exceptions """
        print("An error occurred:", e)
