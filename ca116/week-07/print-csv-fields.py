#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

n = int(input())
p = 0
while p < len(a):
    x = 0
    i = 0
    j = 0
    while i < len(a[p]):
        while i < len(a[p]) and a[p][i] != ',':
            i = i + 1
        if x == n:
            print(a[p][j:i])
            i = len(a[p])
        x = x + 1
        i = i + 1
        j = i
    p = p + 1





# a = []

# s = input()
# while s != "end":
#     b = []
#     i = 0
#     while i < len(s):
#         j = i + 1
#         while j < len(s) and s[j] != ",":
#             j = j + 1
#         if s[i] == ",":
#             b.append(s[i + 1:j])
#         else:
#             b.append(s[i:j])
#         i = j
#     a.append(b)
#     i = i + 1
#     s = input()

# field = int(input())

# i = 0
# while i < len(a):
#     print(a[i][field])
#     i = i + 1



# s = input()
# a = []
# while s != "end":
#     i = 0
#     tmp_a = []
#     while i < len(s):
#         tmp_str = ""
#         while i < len(s) and s[i] != ",":
#             tmp_str = tmp_str + s[i]
#             i = i + 1
#         tmp_a.append(tmp_str)
#         i = i + 1
#     a.append(tmp_a)
#     s = input()

# search = int(input())
# i = 0
# while i < len(a):
#     print(a[i][search])
#     i = i + 1

    
