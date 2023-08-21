#!/usr/bin/env python3

import sys

file = sys.argv[1]

translation = {}
with open(file) as f:
    a = f.readlines()

for word in a:
    word = word.split()
    #  assigns the irish words as values to the english version
    #  translation[word[0]] are the keys, and word[1] would be its corresponding value
    translation[word[0]] = word[1]
    
number = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten" 
}

numbers = sys.stdin.readlines()

for line in numbers:
    digits = line.split()
    words = []
    for digit in digits:
        if digit in number:
            #  you get the translated version rather than the english version
            words.append(translation[number[digit]])
    print(" ".join(words))



#!/usr/bin/env python3

# import sys

# mapping = {}

# with open(sys.argv[1]) as f:
#     lines = f.readlines()
#     for i, l in enumerate(lines):
#         mapping[i] = l.split()[1]

# for line in sys.stdin:
#     output = ""
#     for n in line.split():
#         output += mapping[int(n)] + " "
#     print(output.strip())



#!/usr/bin/env python3

# import sys
# d = {}
# nums = sys.stdin.readlines()
# with open (sys.argv[1]) as f:
# 	tr = f.readlines()

# count = 0
# for line in tr:
# 	line = line.strip().split()
# 	d[str(count)] = (line[0], line[1])
# 	count += 1
# for line in nums:
# 	line = line.strip().split()
# 	s = ""
# 	for n in line:
# 		if n in d:
# 			s += d[n][1] + " "
# 	print(s.strip())




#!/usr/bin/env python3

# import sys

# file = sys.argv[1]
# dict = {}
# filedetails = []

# with open(file, "r") as f_in:
#   for line in f_in:
#     filedetails.append(line.strip())

# for pair in filedetails:
#   pair = pair.split()
#   dict[pair[0]] = pair[1]


# numbers = {"0" : "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten"}

# for line in sys.stdin:
#   line = line.strip().split()
#   fin = " ".join([numbers[num] if num in numbers else "unknown" for num in line])
#   fin = fin.split()
#   print(" ".join([dict[nums] if nums in dict else "unknown" for nums in fin]))
