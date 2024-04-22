#!/usr/bin/python3
'''
export data in the CSV format
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_req = requests.get(user_url, verify=False).json()
    name = user_req.get('username')
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todo_req = todo = requests.get(todo_url, verify=False).json()
    with open(f"{user_id}.csv", 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_req:
            completed = task.get("completed")
            title = task.get("title")
            taskwriter.writerow([int(user_id), name, completed, title])
