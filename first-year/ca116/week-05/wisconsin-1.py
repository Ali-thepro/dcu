#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) - 1:
        if s[i] == "," and (s[i + 1:i + 3] == "WI"):
            print(s[:i])
        i += 1
    s = input()





# s = input()

# while s != "end":
#     i = 0
#     city = ""
#     while s[i] != ",":
#         city = city + s[i]
#         i = i + 1
#     i = i + 1

#     if s[i:(i + 2)] == "WI":
#         print(city)
#     s = input()





# s = input()
# i = 0

# while s != "end":
#     while i < len(s) and s[i] != ",":
#         i = i + 1
#     if s[i] == ","  and s[i + 1:i + 3] == "WI":
#         print(s[:i])

#     i = 0
#     s = input()