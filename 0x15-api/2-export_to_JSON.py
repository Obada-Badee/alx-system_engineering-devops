#!/usr/bin/python3
'''
export data in JSON format
'''

import json
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_req = requests.get(user_url, verify=False).json()
    todo_req = todo = requests.get(todo_url, verify=False).json()

    name = user_req.get('username')

    tasks = [{"task": task.get("title"),
              "username": name,
              "completed": task.get("completed")} for task in todo_req]
    json_rep = {}
    json_rep[user_id] = tasks

    with open(f"{user_id}.json", 'w') as jsfile:
        json.dump(json_rep, jsfile)
