#!/usr/bin/python3
"""export to JSON"""

from json import dump
from os import path, remove
from sys import argv, exit
from requests import get


def main():
    """main function"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    user = get(f'{BASE_URL}users/{id_user}').json()
    todos = get(f'{BASE_URL}/users/{id_user}/todos').json()
    username = user.get("username")
    filename = f"{id_user}.json"
    dt = {id_user: []}
    for task in todos:
        if task.get('userId') == int(id_user):
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            dt[id_user].append(task_dict)

    if path.exists(filename):
        remove(filename)
    with open(filename, 'w') as file:
        dump(dt, file)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./2-export_to_JSON.py <id_user>")
        exit(1)
    main()
