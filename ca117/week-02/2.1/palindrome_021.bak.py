# !/usr/bin/env python3

import sys

def palindrome(line):
    keep = []

    for c in line:
        if c.isalnum():
            keep.append(c)
    return keep == keep[::-1]


for line in sys.stdin:
    line = line.strip().lower()
    print(palindrome(line))




# import sys

# def palindrome(word):
#     final = ([l.lower() for l in word if l.isalnum()])
#     print(final)
#     return final == final[::-1]
    
# def main():
#     for word in sys.stdin:
#         print(palindrome(word.strip()))
# if __name__ == "__main__":
#     main()