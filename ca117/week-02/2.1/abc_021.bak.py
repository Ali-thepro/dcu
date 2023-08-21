#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
# tokens = [int(t) for t in lines[0].strip().split()]
tokens = []
for t in lines[0].strip().split():
    tokens.append(int(t))

order = lines[1].strip()
final_order = ''

for char in order:
    if char == 'C':
        final_order += str(max(tokens)) + ' '
    elif char == 'A':
        final_order += str(min(tokens)) + ' '
    else:
        # print the digit that isnt min or max
        for t in tokens:
            if t != min(tokens) and t != max(tokens):
                final_order += str(t) + ' '
                
print(final_order.strip())






#!/usr/bin/env python3

# import sys
# mylines = sys.stdin.readlines()
# nums = mylines[0].split()
# words = mylines[1].strip()
# mynumbers = []

# for i in nums:
#     mynumbers.append(int(i))
#     mynumbers.sort()

# content = ""
# for chars in words:
#     if chars == "A":
#         content += f"{mynumbers[0]} "
#     elif chars == "B":
#         content += f"{mynumbers[1]} "
#     elif chars == "C":
#         content += f"{mynumbers[2]} "
# print(content.strip())






#!/usr/bin/env python3

# import sys

# a, b, c = sorted([int(x) for x in input().split()])
# order = input().strip()

# numbers = {'A': a, 'B': b, 'C': c}

# output = [numbers[x] for x in order]

# print(" ".join(str(x) for x in output))