#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != " ":
    i = i + 1
day = s[:i]

j = i + 1
while j < len(s) and s[j] != " ":
    j = j + 1
date = s[i + 1:j]

k = 0
while k < len(s) and s[k] != ",":
    k = k + 1
month = s[j + 1:k]
year = s[k + 1:]

print(month, date + ',' + year, '(' + day + ')')
