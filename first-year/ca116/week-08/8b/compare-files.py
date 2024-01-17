#!/usr/bin/env python3

import sys

args = sys.argv[1:]

file1 = args[0]
file2 = args[1]

with open(file1) as f1:
    a_lines = f1.readlines()

with open(file2) as f2:
    b_lines = f2.readlines()

if len(a_lines) < len(b_lines):
    print(len(b_lines) - len(a_lines), 0)
elif len(b_lines) < len(a_lines):
    print(len(a_lines) - len(b_lines), 0)

i = 0
while i < len(a_lines) and i < len(b_lines):
    a_string = a_lines[i]
    b_string = b_lines[i]
    char_pos = 0
    while char_pos < len(a_string):
        if a_string[char_pos] != b_string[char_pos]:
            print(i, char_pos)
        char_pos += 1
    i += 1
