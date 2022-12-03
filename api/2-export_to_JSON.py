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
    employee_name = ''
    if user_response['id'] == int(user_id):
        employee_name = user_response['username']

    container = {"{}".format(sys.argv[1]): []}
    key = "{}".format(sys.argv[1])
    for task in response:
        to_dump = {}
        to_dump['task'] = task['title']
        to_dump['username'] = user_response['username']
        to_dump['completed'] = task['completed']
        container[key].append(to_dump)
        with open("{}.json".format(sys.argv[1]), 'a+') as f:
            json.dump(container, f)
