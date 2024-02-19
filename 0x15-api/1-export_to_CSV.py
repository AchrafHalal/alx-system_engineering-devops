#!/usr/bin/python3
"""export to CSV"""
from sys import argv, exit
import csv
import requests
from os import path, remove


def main():
    """main function"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    user = requests.get(f'{BASE_URL}users/{id_user}').json()
    todos = requests.get(f'{BASE_URL}/users/{id_user}/todos').json()
    filename = f"{id_user}.csv"
    username = user.get("username")

    if path.exists(filename):
        remove(filename)

    with open(filename, 'w') as file:
        for task in todos:
            if task.get('userId') == int(id_user):
                done = task.get("completed")
                title = task.get("title")
            file.write(f'"{id_user}","{username}","{done}","{title}"\n')


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <id_user>")
        exit(1)
    main()
