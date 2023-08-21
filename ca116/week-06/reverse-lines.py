#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a) / 2:
    tmp = a[i]
    a[i] = a[len(a) - i - 1]
    a[len(a) - i - 1] = tmp
    i = i + 1

i = 0
while i < len(a):
    print(a[i])
    i = i + 1






#!/usr/bin/env python3

# lines = []

# s = input()
# while s != "end":
#     lines.append(s)
#     s = input()

# i = 0
# while i < len(lines):
#     print(lines[len(lines) - i - 1])
#     i = i + 1

