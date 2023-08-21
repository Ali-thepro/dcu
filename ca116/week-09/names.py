#!/usr/bin/env python3

import sys

boys = {}
girls = {}
with open("boys.txt") as f:
    s = f.readline().rstrip()
    while 0 < len(s):
        boys[s] = True
        s = f.readline().rstrip()
with open("girls.txt") as f:
    s = f.readline().rstrip()
    while 0 < len(s):
        girls[s] = True
        s = f.readline().rstrip()

names = sys.stdin.readlines()
i = 0
while i < len(names):
    name = names[i].rstrip()
    if name in boys and name in girls:
        print(name, "either")
    elif name in boys:
        print(name, "boy")
    else:
        print(name, "girl")
    i = i + 1
