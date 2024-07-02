# Task 1

import os



def list_directory_contents(path):
    for i in os.listdir(path):
        print(i)


while True:

    path_input = input("Please choose a directory that you would like to view: ")

    try:
        list_directory_contents(path_input)
        break

    except FileNotFoundError:
        print(f"Path {path_input} was not found.  Please try again.")
