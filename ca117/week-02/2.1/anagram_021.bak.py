#!/usr/bin/env python3
 
'''Check if strings are anagrams.'''
 
import sys
 
def anagram(left, right):
     # act cat anagrams
     # act cats not anagrams
    for c in left:
        if c not in right:
            return False
        right = right.replace(c, '', 1)
    # right must now be empty
    return not right
 
for line in sys.stdin:
    [left, right] = line.strip().split()
    print(anagram(left, right))
