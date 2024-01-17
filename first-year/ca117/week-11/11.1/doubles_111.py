import sys

def double_vowels(word):
    vowels = 'aeiou'
    count = 0
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i] == word[i + 1]:
            count += 1
    return count

words = [line.strip() for line in sys.stdin]
print(max(words, key=double_vowels))