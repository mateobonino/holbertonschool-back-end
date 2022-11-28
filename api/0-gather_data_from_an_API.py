#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    get_name = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(
        url,
        params={'userId': int(user_id)})
    user_response = requests.get(
        get_name,
        params={'id': int(user_id)})
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks_text = []

    for key in response.json():
        if key['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
            tasks_text.append(key['title'])
        TOTAL_NUMBER_OF_TASKS += 1
    EMPLOYEE_NAME = ''
    for name in user_response.json():
        if 'name' in name.keys():
            employee_name = name['name']

    to_print = f"Employee {EMPLOYEE_NAME} is done with tasks"
    to_print += f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})"
    for TASK_TITLE in tasks_text:
        print("\t {}".format(TASK_TITLE))
