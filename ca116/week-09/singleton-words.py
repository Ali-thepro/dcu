#!/usr/bin/env python3

import sys

words = {}

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1
    word = sys.stdin.readline().rstrip()

for word in words:
    if words[word] == 1:
        print(word)




#!/usr/bin/env python3

# import sys

# s = sys.stdin.readlines()
# words = {}
# i = 0
# while i < len(s):
#     words[s[i].rstrip()] = s[i].rstrip() not in words
#     i = i + 1

# for k in words:
#     if words[k]:
#         print(k)