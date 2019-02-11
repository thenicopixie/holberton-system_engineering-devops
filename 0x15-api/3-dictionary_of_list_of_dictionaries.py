#!/usr/bin/python3
"""Script that exports data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for u in users:
        uId = u.get('id')
        username = u.get("username")
        data[uId] = []
        url = 'https://jsonplaceholder.typicode.com/todos?userId='
        todos = requests.get(url + str(uId)).json()
        for d in todos:
            data[uId].append({
                "username": username,
                "task": d.get("title"),
                "completed": d.get("completed")
            })
    with open("todo_all_employees.json", 'w') as fn:
        json.dump(data, fn)
