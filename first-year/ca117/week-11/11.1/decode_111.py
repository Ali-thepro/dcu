import sys

vowels = 'aeiou'
def decode(words):
    for vowel in vowels:
        words = words.replace(vowel + 'p' + vowel, vowel)
    return words


for line in sys.stdin:
    print(decode(line.strip()))