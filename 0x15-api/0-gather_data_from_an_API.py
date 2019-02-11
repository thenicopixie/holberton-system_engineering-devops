#!/usr/bin/python3
"""Script that returns information about a user's TODO list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1]).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1]).json()
    username = user.get('name')
    completed = [c.get('title') for c in todos if c.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
          username, len(completed), len(completed)))
    for task in completed:
        print("\t {}".format(task))
