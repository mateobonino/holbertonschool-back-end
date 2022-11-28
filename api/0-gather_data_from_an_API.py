#!/usr/bin/python3
import requests
import json
import sys
"""
For a given employee ID, returns information about his/her TODO list progress.
"""
user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
get_name = "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
response = requests.get(url)
user_response = requests.get(get_name)
user_result = user_response.json()
result = response.json()
count = 0
tasks_text = []
for key in result:
    if key['completed'] is True:
        count += 1
        tasks_text.append(key['title'])
employee_name = ''
for name in user_result:
    if 'name' in name.keys():
        employee_name = name['name']

print("Employee {} is done with tasks({}/20):".format(employee_name, count))
for task in tasks_text:
    print("     {}".format(task))
