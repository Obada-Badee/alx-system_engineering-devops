#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
'''

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        userId = argv[1]
        url = "https://jsonplaceholder.typicode.com"
        req = requests.get(f"{url}/users/{userId}")
        name = req.json().get("name")
        
        if name is not None:
            todo_req = requests.get(f"{url}/todos?userId={userId}").json()
            at_c = len(todo_req) #at_c = all tasks count
            completed_tasks = []

            for task in todo_req:
                if task.get("completed") is True:
                    completed_tasks.append(task)

            ct_c = len(completed_tasks) #ct_c == completed task count

            print(f"Employee {name} is done with tasks({ct_c}/{at_c}):")

            for titles in completed_tasks:
                title = titles.get("title")
                print(f"\t {title}")
