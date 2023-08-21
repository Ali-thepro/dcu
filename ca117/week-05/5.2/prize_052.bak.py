#!/usr/bin/env python3

import sys

start = sys.stdin.readline().strip()
order = sys.stdin.readline().strip()
prize = "123"
prize = list(prize.replace(start, "0"))
for char in order:
    if char == "A":
        prize[0], prize[1] = prize[1], prize[0]
    elif char == "B":
        prize[1], prize[2] = prize[2], prize[1]
    elif char == "C":
        prize[0], prize[2] = prize[2], prize[0]
print(prize.index("0") + 1)



# import sys

# d = {'A': (1, 2), 'B': (2, 3), 'C': (1, 3)}

# locs = [0, 0, 0, 0]

# start = int(sys.stdin.readline().strip())

# locs[start] = 1

# swaps = sys.stdin.readline().strip()

# for swap in swaps:
#         i, j = d[swap]
#         locs[i], locs[j] = locs[j], locs[i]


# print(locs.index(1))



# import sys

# inputs = sys.stdin.readlines()
# pos = int(inputs[0])
# letters = inputs[1].strip()

# def a(prize):
# 	if prize == 1:
# 		prize = 2
# 	elif prize == 2:
# 		prize = 1
# 	return prize

# def b(prize):
# 	if prize == 2:
# 		prize = 3
# 	elif prize == 3:
# 		prize = 2
# 	return prize

# def c(prize):
# 	if prize == 3:
# 		prize = 1
# 	elif prize == 1:
# 		prize = 3
# 	return prize
	
# for l in letters:
# 	if l == "A":
# 		pos = a(pos)
# 	elif l == "B":
# 		pos = b(pos)
# 	else:
# 		pos = c(pos)
# print(pos)
