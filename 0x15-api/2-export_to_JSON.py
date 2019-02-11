#!/usr/bin/python3
"""Script that exports data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todos = requests.get(url + sys.argv[1]).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1]).json()
    uId = user.get('id')
    username = user.get('username')
    data = {}
    data[uId] = []
    for d in todos:
        data[uId].append({
            "task": d.get("title"),
            "completed": d.get("completed"),
            "username": d.get("username"),
        })
    with open("{}.json".format(sys.argv[1]), 'w') as fn:
        json.dump(data, fn)
