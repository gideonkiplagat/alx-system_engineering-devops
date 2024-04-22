#!/bin/python3

"""
task #0, extend your Python script to export data in the JSON format.
"""
from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()

    row = []
    response1 = get('https://jsonplaceholder.typicode.com/users')
    data1 = response1.json()

    new_dict = {}
    for j in data1:
        row = []
        for i in data:
            new_dict1 = {}
            if j['id'] == i['userId']:
                new_dict1['username'] = j['username']
                new_dict1['task'] = i['title']
                new_dict1['completed'] = i['completed']
                row.append(new_dict1)

        new_dict1[j['id']] = row
    
    with open("todo_all_employees.json", mode='w') as file:
        json_obj = json.dumps(new_dict1)
        file.write(json_obj)

