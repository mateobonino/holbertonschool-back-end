#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
"""


import requests
import sys


def request_api():
    """
    Makes a request to the JSONPlaceholder API
    """
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    get_name = f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    response = requests.get(url)
    user_response = requests.get(get_name)
    count = 0
    total_tasks = 0
    tasks_text = []

    for key in response.json():
        if key['completed'] is True:
            count += 1
            tasks_text.append(key['title'])
        total_tasks += 1
    employee_name = ''
    for name in user_response.json():
        if 'name' in name.keys():
            employee_name = name['name']

    print("Employee {} is done with tasks({}/{})):".format(employee_name,
                                                           count,
                                                           total_tasks))
    for task in tasks_text:
        print("\t {}".format(task))


if __name__ == '__main__':
    request_api()
