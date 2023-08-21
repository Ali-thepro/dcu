import sys

lines = [l.strip() for l in sys.stdin.readlines()]
vowels, wordDict = 'aeiou', {}

for word in lines:
    wordDict[word] = 0
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i] == word[i + 1]:
            wordDict[word] += 1

print(max(wordDict, key=wordDict.get))



# import sys

# lines = [l.strip() for l in sys.stdin.readlines()]
# vowels, wordDict = 'aeiou', {}

# for word in lines:
#     wordDict[word] = 0
#     for i in range(1, len(word)):
#         if word[i] in vowels and word[i] == word[i - 1]:
#             wordDict[word] += 1

# mostDoubles = max(wordDict.values())
# print(" ".join([word for word in wordDict if wordDict[word] == mostDoubles]))

# for key, value in wordDict.items():
#     if value == mostDoubles:
#         print(key)




# import sys

# vowels = ['a', 'e', 'i', 'o', 'u']

# def double_vowels(word):
#     count = 0
#     for v in vowels:
#         if v in word and (word[word.index(v)] == word[word.index(v) + 1]):
#             count += 1
#     return count

# words = [line.strip() for line in sys.stdin]
# print(max(words, key=double_vowels))