#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employees """
import csv
import requests
import sys

""""""
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Get user ID 
    userid = sys.argv[1]

    # Fetch user data from API
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    username = json_o.get('username')  # Store username

    # Fetch todos  user  API
    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()

    # For each todo, keep relevant data in tasking_ing
    tasking_ing = []
    for task in tasks:
        tasking_ing.append([userid,
                       username,
                       task.get('completed'),
                       task.get('title')])

    # We write data to CSV file
    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasking_ing:
            # list in tasking_ing as a new row in the CSV file
            employee_writer.writerow(task)
