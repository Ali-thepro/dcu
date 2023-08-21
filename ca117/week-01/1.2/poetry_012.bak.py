import sys
sentences = sys.stdin.readlines()

a = []
for sentence in sentences:
    sentence.strip()
    a.append(len(sentence))
x = max(a)
x = x - 1

for sentence in sentences:
    sentence = sentence.strip()
    print(f"{sentence:^{x}}")



#!/usr/bin/env python3
# import sys
# poetry = sys.stdin.readlines()
# line = "".join(poetry).rstrip()
# line = line.split("\n")

# max_length = max(map(len, line))
# for word in line:
#     print(f"{word:^{max_length}}")




# import sys

# lines = sys.stdin.readlines()

# def getMax1(word, maximum=0):
#     maximum = max([len(word.strip()) for word in lines])
#     return maximum

# def output(word):
#     maximum = getMax1(word)
#     return f'{word:^{maximum}}'
    
# for line in lines:
#     print(output(line.strip()))