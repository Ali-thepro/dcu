#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][len(files[i]) - 3:] == ".py":
        with open(files[i]) as f:
            if len(f.read()) > 0:
                print(files[i])
    i = i + 1
