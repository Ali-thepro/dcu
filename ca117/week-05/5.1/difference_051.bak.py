#!/usr/bin/env python3

import sys

line1, line2 = sys.stdin.read().split()
print(line1)
print(line2)
z = []
for a,b in zip(line1, line2):
    if a != b:
        z.append('*')
    else:
        z.append('-')
print(''.join(z))




# line1, line2 = [n.strip() for n in sys.stdin]
# print(line1)
# print(line2)

# z = ['*' if a != b else '-' for a,b in zip(line1, line2)]
# print(''.join(z))

# for line in sys.stdin:
#     line = [n.strip() for n in line]
#     print(line)



#!/usr/bin/env python3

# import sys

# lines = sys.stdin.readlines()
# first = lines[0].strip()
# second = lines[1].strip()
# s = "" 
# for i in range(len(first)):
# 	if first[i] == second[i]:
# 		s += "-"
# 	else:
# 		s += "*"
# print(first)
# print(second)
# print(s)





#!/usr/bin/env python3

# import sys

# lines = sys.stdin.read().split()

# first = lines[0]
# second = lines[1]

# i = 0
# while i < len(first):

#     j = 0
#     differences = ""
#     while j < len(first) and len(second):
#         if first[j] == second[j]:
#             differences += "-"
#         if first[j] != second[j]:
#             differences += "*"
#         j += 1

#     i += 1

# print(first)
# print(second)
# print(differences)