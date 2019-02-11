#!/usr/bin/python3
"""Script that exports data in the CSV format"""
import csv
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
    with open("{}.csv".format(sys.argv[1]), 'w') as fn:
        writer = csv.DictWriter(fn, fieldnames=['id', 'username', 'completed',
                                                'title'],
                                quoting=csv.QUOTE_ALL)
        for data in todos:
            writer.writerow({
                'id': uId,
                'username': username,
                'completed': data.get('completed'),
                'title': data.get('title'),
            })
