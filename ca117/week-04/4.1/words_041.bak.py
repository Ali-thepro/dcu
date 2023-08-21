#!/usr/bin/env python3

import sys
import string

freq = {}
punct = string.punctuation

for line in sys.stdin:
    line = line.strip().lower().split()
    for word in line:
        word = word.strip(punct)
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

for k, v in sorted(freq.items()):
    print(f"{k} : {v}")


#!/usr/bin/env python3

import sys
import string

freq = {}
punct = string.punctuation
punct = punct.replace("'", "")

for line in sys.stdin:
    line = line.strip().lower().split()
    for word in line:
        word = word.strip()
        for ch in word:
            if ch in punct:
                word = word.replace(ch, "")
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

for k, v in sorted(freq.items()):
    print(f"{k} : {v}")





#!/usr/bin/env python3

# import sys
# import string

# lines = sys.stdin.readlines()
# count = {}
# for line in lines:
#     words = line.strip().lower().split()
#     for word in words:
#         word = word.rstrip(string.punctuation)

#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1

# for word in sorted(count.keys()):
#     print(f"{word} : {count[word]}")