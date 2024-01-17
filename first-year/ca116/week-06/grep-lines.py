#!/usr/bin/env python3

import sys

args = sys.argv[1:]

a = []
s = input()
i = 0

while s != "end":
    i = 0
    while i < len(s):
        if s[i:i + len(args[0])] == args[0]:
            a.append(s)
            i = i + len(s)
        else:
            i = i + 1
    s = input()

j = 0
while j < len(a):
    print(a[j])
    j = j + 1



#blott solution
#!/usr/bin/env python3

# import sys
# pattern = sys.argv[1]

# line = input()
# while line != "end":
#    i = 0
#    while i < len(line) and line[i:i + len(pattern)] != pattern:
#       i = i + 1

#    if i < len(line):
#       print(line)
#    line = input()