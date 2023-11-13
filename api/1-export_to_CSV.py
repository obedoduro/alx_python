#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Get user ID from command line arguments
    userid = sys.argv[1]

    # Fetch user data from API
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    username = json_o.get('username')  # Store username

    # Fetch todos for user from API
    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()

    # For each todo, store relevant data in l_task
    l_task = []
    for task in tasks:
        l_task.append([userid,
                       username,
                       task.get('completed'),
                       task.get('title')])

    # Write data to CSV file
    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in l_task:
            # Write each list in l_task as a new row in the CSV file
            employee_writer.writerow(task)
