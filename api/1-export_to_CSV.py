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
    get_name = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(
        url,
        params={'userId': int(user_id)})
    user_response = requests.get(get_name).json()
    employee_name = ''
    if user_response['id'] == int(user_id):
        employee_name = user_response['username']

    for key in response.json():
        with open('{}.csv'.format(sys.argv[1]), 'a+') as f:
            f.write('"{}","{}","{}","{}"\n'.format(user_id,
                                                   employee_name,
                                                   key['completed'],
                                                   key['title']))
    f.close()
