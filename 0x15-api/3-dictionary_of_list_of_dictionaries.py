#!/usr/bin/python3
'''
export all data from API
'''

import json
import requests

if __name__ == '__main__':

    users_url = f"https://jsonplaceholder.typicode.com/users/"
    users_req = requests.get(users_url, verify=False).json()

    json_rep = {}

    for user in users_req:
        name = user.get('username')
        u_id = user.get('id')

        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
        todo_req = todo = requests.get(todo_url, verify=False).json()

        tasks = [{"username": name,
                  "task": task.get("title"),
                  "completed": task.get("completed")} for task in todo_req]

        json_rep[u_id] = tasks

    with open(f"todo_all_employees.json", 'w') as jsfile:
        json.dump(json_rep, jsfile)
