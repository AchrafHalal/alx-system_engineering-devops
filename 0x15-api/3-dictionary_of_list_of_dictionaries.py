#!/usr/bin/python3
"""export to JSON"""

from json import dump
from os import path, remove
from requests import get


def main():
    """main function"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    filename = "todo_all_employees.json"
    users = get(f'{BASE_URL}users').json()
    dt = {}
    for user in users:
        id_user = user.get("id")
        username = user.get("username")
        todos = get(f'{BASE_URL}/users/{id_user}/todos').json()
        user_dt = []
        for task in todos:
            if task.get('userId') == int(id_user):
                task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                }
                user_dt.append(task_dict)
        dt[id_user] = user_dt
    if path.exists(filename):
        remove(filename)
    with open(filename, 'w') as file:
        dump(dt, file)


if __name__ == "__main__":
    main()
