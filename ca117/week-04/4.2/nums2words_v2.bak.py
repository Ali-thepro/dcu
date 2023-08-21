#!/usr/bin/env python3

import sys

numbers = {"0" : "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten"}

for line in sys.stdin:
  line = line.strip().split()
  print(" ".join([numbers[num] if num in numbers else "unknown" for num in line]))




#!/usr/bin/env python3

# import sys

# numbers = sys.stdin.readlines()

# number = {
#     "0" : "zero",
#     "1" : "one",
#     "2" : "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "10": "ten" 
# }

# for line in numbers:
#     digits = line.split()
#     #  list needs to be within for loop not outside of it
#     words = []
#     #  individual number
#     for digit in digits:
#         #  if it's in the dictionary
#         if digit in number:
#             #  append to list
#             words.append(number[digit])
#         else:
#             #  else append "unknown"
#             words.append("unknown")
#     #  print the output
#     print(" ".join(words))





#!/usr/bin/env python3

# import sys

# lines = sys.stdin.readlines()
# d = {
#     0: "zero",
# 	1: "one",
# 	2: "two",
# 	3: "three",
# 	4: "four",
# 	5: "five",
# 	6: "six",
# 	7: "seven",
# 	8: "eight",
# 	9: "nine",
#    10: "ten"
# }

# for line in lines:
# 	line = line.strip().split()
# 	s = ""
# 	for n in line:
# 		if int(n) in d:
# 			s += d[int(n)] + " "
# 		else:
# 			s += "unknown" + " "
# 	print(s.strip())




#!/usr/bin/env python3

# import sys

# numbers = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     10: "ten"
# }

# for line in sys.stdin:
#     output = ""
#     nums = line.split()
#     for n in nums:
#         try:
#             output += numbers[int(n)] + " "
#         except (KeyError, ValueError):
#             output += "unknown "
#     print(output.strip())