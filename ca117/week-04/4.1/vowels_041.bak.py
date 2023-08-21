#!/usr/bin/env python3

import sys

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

def count_vowels(line, letter):
    count = line.count(letter)
    return count

def tagger(item):
    return item[1]

for line in sys.stdin:
    line = line.lower().rstrip()
    for letters in vowels:
        vowels[letters] += count_vowels(line, letters)

padding = len(str(max(vowels.values())))


for k, v in sorted(vowels.items(), key=tagger, reverse=True):
    print(f"{k} : {v:{padding}}")



#!/usr/bin/env python3


# import sys

# vowels = {"e" : 0, "a" : 0, "o" : 0, "i" : 0, "u" : 0}

# for line in sys.stdin:
#     line = line.strip().lower()
#     for word in line:
#         if word in vowels:
#             vowels[word] += 1

# def tagger(item):
#     return item[1]

# padding = len(str(max(vowels.values())))
# for k, v in sorted(vowels.items(), key=tagger, reverse=True):
#     print(f'{k} : {v:>{padding}}')


# import sys
# for line in sys.stdin:
#     line = line.strip().lower().split()
#     for word in line:
#         for ch in word:
#             if ch in d:
#                 d[ch] = d.get(ch) + 1
# def tagger(s):
#     return s[1]
# width = len(str(max(d.values())))
# for k,v in sorted(d.items(), key=tagger, reverse=True):
#     print(f'{k} : {v:>{width}}')