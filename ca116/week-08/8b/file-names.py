#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
    a = s.split("/")
    print(a[len(a) - 1])
    s = sys.stdin.readline().rstrip()



# import sys

# files = sys.stdin.readlines()
# i = 0
# while i < len(files):
#     f = files[i].split("/")
#     print(f[len(f) - 1].rstrip())
#     i = i + 1
