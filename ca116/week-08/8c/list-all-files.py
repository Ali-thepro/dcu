#!/usr/bin/env python3

import os

directories = ["."]

while 0 < len(directories):

    directory = directories.pop()
    entries = os.listdir(directory)
    i = 0
    while i < len(entries):
        entry = directory + "/" + entries[i]
        if os.path.isfile(entry):
            print(entry)
        if os.path.isdir(entry):
            directories.append(entry)
        i = i + 1




# import os
# todo = ["."]

# i = 0
# while i < len(todo):
#     curr_path = todo[i]
#     files = os.listdir(curr_path)
#     j = 0
#     while j < len(files):
#         curr_file = curr_path + "/" + files[j]
#         if os.path.isfile(curr_file):
#             print(curr_file)
#         else:
#             todo.append(curr_file)
#         j = j + 1
#     i = i + 1
