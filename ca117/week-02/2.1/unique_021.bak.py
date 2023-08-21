#!/usr/bin/env python3


import sys
import string


unique = []
for line in sys.stdin:
    line = line.strip().lower().split()
    for word in line:
        word = word.strip(string.punctuation)
        if len(word) > 0 and word not in unique:
            unique.append(word)
print(len(unique))





# import sys
# import string

# tokens = sys.stdin.readlines()
# unique = []
# for token in tokens:
#     token = token.strip().lower()
#     for char in token:
#         if char in string.punctuation:
#             token = token.replace(char, "")
#     token = token.split()
#     for word in token:
#         if word not in unique and len(word) > 0:
#             unique.append(word)
# print(len(unique))







# import sys
# import string

# tokens = sys.stdin.readlines()
# token_set = set()
# for token in tokens:
#     token = token.strip().lower()
#     for char in token:
#         if char in string.punctuation:
#             token = token.replace(char, "")
#     token = token.split(" ")
#     for word in token:
#         if 0 < len(word):
#             token_set.add(word)
# print(len(token_set))



# import sys
# import string
# lines = sys.stdin.readlines()
# ordered = []

# for line in lines:
#     tokens = line.strip().split()
#     for words in tokens:
#         words = words.lower()
#         for punc in words:
#             if punc in string.punctuation:
#                 words = words.replace(punc, "", 1)

#         if words not in ordered and len(words) > 0:
#             ordered.append(words)

# print(len(ordered))