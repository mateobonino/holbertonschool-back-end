#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import json
import sys


user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
get_name = "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
response = requests.get(url)
user_response = requests.get(get_name)
result = response.json()
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

print("Employee {} is done with tasks({}/{})):".format(employee_name, count,
                                                       total_tasks))
for task in tasks_text:
    print("     {}".format(task))
