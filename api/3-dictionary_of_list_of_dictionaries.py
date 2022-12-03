#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    get_name = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(
        url,
        params={'userId': int(user_id)}).json()
    user_response = requests.get(get_name).json()

    key = "{}".format(sys.argv[1])
    container = {}
    container[key] = []
    for task in response:
        to_dump = {}
        to_dump['task'] = task.get('title')
        to_dump['username'] = user_response['username']
        to_dump['completed'] = task.get('completed')
        container[key].append(to_dump)
        with open("todo_all_employees.json", 'w+') as f:
            json.dump(container, f)
