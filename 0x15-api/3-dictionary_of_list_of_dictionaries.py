#!/usr/bin/python3

"""
task #0, extend your Python script to export data in the JSON format.
"""
from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos')
    todos_data = response.json()

    response1 = get('https://jsonplaceholder.typicode.com/users')
    users_data = response1.json()

    all_users_tasks = {}
    for user in users_data:
        user_tasks = []
        for todo in todos_data:
            if user['id'] == todo['userId']:
                task_info = {
                    'username': user['username'],
                    'task': todo['title'],
                    'completed': todo['completed']
                }
                user_tasks.append(task_info)

        all_users_tasks[user['id']] = user_tasks

    with open("todo_all_employees.json", mode='w') as file:
        json_obj = json.dumps(all_users_tasks)
        file.write(json_obj)
