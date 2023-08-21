#!/usr/bin/env python3

import sys

english = "one two three four five six seven eight nine ten".split()
german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()

translations = {}

i = 0
while i < len(english):
    translations[english[i]] = german[i]
    i = i + 1

word = sys.stdin.readlines()
i = 0
while i < len(word):
    if word[i].rstrip() in translations:
        print(translations[word[i].rstrip()])
    i = i + 1





#!/usr/bin/env python3

# import sys

# numbers = {
#     "one": "eins",
#     "two": "zwei",
#     "three": "drei",
#     "four": "vier",
#     "five": "funf",
#     "six": "sechs",
#     "seven": "sieben",
#     "eight": "acht",
#     "nine": "neun",
#     "ten": "zehn"
# }

# words = sys.stdin.readlines()
# i = 0
# while i < len(words):
#     print(numbers[words[i].rstrip()])
#     i = i + 1
