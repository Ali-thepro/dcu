#!/usr/bin/env python3

import sys

tokens = sys.stdin.readline().split()
# nums = [int(i) for i in tokens]
nums = []
for i in tokens:
    nums.append(int(i))

nums = sorted(nums)

abc = {
    "a": nums[0],
    "b": nums[1],
    "c": nums[2],
    "d": nums[3],
    "e": nums[4],
    "f": nums[5],
}
order = sys.stdin.readline().strip().lower()
output = ""

for letter in order:
    output += f"{abc[letter]} "

print(output.strip())
# #print(output[:-1])



#!/usr/bin/env python3

# import sys

# numbers = sys.stdin.readline().rstrip().split()
# letterinput = sys.stdin.readline().rstrip()
# numbers = sorted([int(n) for n in numbers])
# numbers = [str(n) for n in numbers]
# letters = "ABCDEF"

# dict = dict(zip(letters, numbers))
# print(" ".join([dict[char] for char in letterinput]))



#!/usr/bin/env python3

# import sys

# d = {}
# lines = sys.stdin.readlines()
# nums = lines[0].strip().split()
# letters = lines[1].strip()
# order = sorted(lines[1].strip())
# nums = sorted([int(n) for n in nums])
# zipped = zip(order, nums)


# for tup in zipped:
# 	d[tup[0]] = tup[1]
# s = ""
# for c in letters:
# 	s += str(d[c])+ " "
# print(s.strip())




#!/usr/bin/env python3

# import sys

# tokens = sys.stdin.readline().split()
# numbers = [int(t) for t in tokens]
# sorted = sorted(numbers)

# order = sys.stdin.readline().strip()
# letter = "ABCDEF"

# z = zip(letter, sorted)

# d = {k : v for k, v in z}


# output = [str(d[letter]) for letter in order]
# print(" ".join(output))
