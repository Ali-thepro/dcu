#!/usr/bin/env python3

with open("a.txt") as f:
   words1 = f.readlines()
with open("b.txt") as f:
   words2 = f.readlines()

words = words1 + words2
d = {}

i = 0
while i < len(words):
   if words[i] in words1 and words[i] in words2:
      d[words[i].rstrip()] = True
   i = i + 1

for k in d:
   print(k)


# with open("a.txt") as f:
#    a = f.readlines()
# with open("b.txt") as f:
#    b = f.readlines()

# d = {}

# i = 0
# while i < len(a):
#    if a[i] in b:
#       d[a[i]] = "true"
#    i = i + 1

# if d != {}:
#    print("".join(d).rstrip())




# import sys

# with open("a.txt") as f:
#     n = f.readlines()
# with open("b.txt") as f_out:
#     m = f_out.readlines()

# file1 = {}
# i = 0
# while i < len(n):
#     word = n[i].strip()
#     if word not in file1:
#         file1[word] = True
#     i += 1
# i = 0
# while i < len(m):   #can also use for loop version in seconf method instead of this while loop
#     word = m[i].strip()
#     if word in file1:
#         print(word)
#     i += 1

# with open("a.txt") as f:
#     a = f.readlines()
# with open("b.txt") as f:
#     b = f.readlines()

# seen = {}

# i = 0
# while i < len(a):
#     seen[a[i].rstrip()] = False
#     i += 1
# i = 0
# while i < len(b):
#     if b[i].rstrip() in seen:
#         seen[b[i].rstrip()] = True
#     i += 1
# for k in seen:
#     if seen[k]:
#         print(k)
