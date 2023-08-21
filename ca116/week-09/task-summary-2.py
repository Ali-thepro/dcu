#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
users = {}

i = 0
while i < len(s):
    curr_file = s[i].rstrip().split(".")
    user_id = curr_file[0].split('/')[0].split('-')[1]
    if user_id not in users:
        users[user_id] = []

    if curr_file[2] == 'correct':
        users[user_id].append(curr_file[0])
    elif curr_file[0] in users[user_id]:
        users[user_id].remove(curr_file[0])

    i += 1

i = 0
while i < len(users):
    print('user-' + str(i + 1), len(users[str(i + 1)]))
    i += 1
