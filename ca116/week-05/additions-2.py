#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != "+":
        j = j + 1
    total = total + int(s[i:j])
    i = j + 1

print(total)




# n = 5
# total = 0
# start = 0

# s = input()

# i = 0
# while i < n:
#    p = start
#    while p < len(s) and s[p] != "+":
#       p = p + 1

#    total = total + int(s[start:p])
#    start = p + 1

#    i = i + 1

# print(total)