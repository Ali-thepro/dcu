#!/usr/bin/env python3

seen = []

s = input()
while s != "end":
    i = 0
    while i < len(seen) and seen[i] != s:
        i = i + 1

    if i == len(seen):
        print(s)
        seen.append(s)
    
    s = input()



# a = []

# s = input()
# while s != "end":
#     i = 0
#     while i < len(a) and a[i] != s:
#         i = i + 1
#     if i == len(a):
#         a.append(s)
#     s = input()

# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 1
