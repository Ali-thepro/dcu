#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
    if "a" <= s[i] and s[i] <= "z":
        t = t + chr(ord(s[i]) - ord("a") + ord("A"))
    else:
        t = t + s[i]
    i = i + 1
print(t)



# s = input()
# i = 0
# n = 0
# t = ""
# while i < len(s):
#     if "a" <= (s[i]) <= "z":
#         n = ord(s[i])
#         n -= 32
#         t += chr(n)
#     else:
#         t += s[i]
#     i += 1

# print(t)



# s = input()
# i = 0
# n = 0
# t = ""
# while i < len(s):
#     if 97 <= ord(s[i]) <= 122:
#         n = ord(s[i])
#         n -= 32
#         t += chr(n)
#     else:
#         t += s[i]
#     i += 1

# print(t)