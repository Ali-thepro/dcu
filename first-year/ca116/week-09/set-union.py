#!/usr/bin/env python3

import sys

with open("a.txt") as f:
    words1 = f.readlines()
with open("b.txt") as f:
    words2 = f.readlines()
seen = {}

words = words1 + words2
list = "".join(words).strip()
words = list.split()

i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = True
    i += 1

for k in seen:
    print(k)



# import sys

# with open("a.txt") as f:                                   
#     a = f.readlines()
# with open("b.txt") as f_out:
#     b = f_out.readlines()
# seen = {}

# i = 0
# while i < len(a):
#     word = a[i].strip()
#     if word not in seen:
#         seen[word] = True
#     i += 1

# i = 0
# while i < len(b):
#     word = b[i].strip()
#     if word not in seen:
#         seen[word] = True
#     i += 1

# for k in seen:
#     print(k)





# with open("a.txt") as f:
#     a = f.readlines()
# with open("b.txt") as f:
#     b = f.readlines()

# seen = {}

# i = 0
# while i < len(a):
#     if a[i].rstrip() not in seen:
#         seen[a[i].rstrip()] = True
#     i += 1
# i = 0
# while i < len(b):
#     if b[i].rstrip() not in seen:
#         seen[b[i].rstrip()] = True
#     i += 1

# for k in seen:
#     print(k)