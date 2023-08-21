import sys

vowels = 'aeiou'

for line in sys.stdin:
    words = line.strip().split()
    for vowel in vowels:
        words = [word.replace(vowel + 'p' + vowel, vowel) for word in words]
    print(' '.join(words))



# import sys

# vowels = 'aeiou'

# for line in sys.stdin:
#     for vowel in vowels:
#         for ch in line:
#             line = line.replace(vowel + 'p' + vowel, vowel)
#     print(line.strip())





# import sys

# lines = [l.strip() for l in sys.stdin.readlines()]
# vowels = 'aeiou'

# for word in lines:
#     newStr = ''
#     i = 0
#     while i < len(word):
#         if word[i] not in vowels:
#             newStr += word[i]
#         else:
#             newStr += word[i]
#             i += 2
#         i += 1
#     print(newStr)




# import sys
# vowels = 'aeiou'

# for word in sys.stdin:
#     newStr = ''
#     i = 0
#     while i < len(word):
#         if word[i] not in vowels:
#             newStr += word[i]
#         else:
#             newStr += word[i]
#             i += 2
#         i += 1
#     print(newStr.strip())






# import sys

# vowels = 'aeiou'
# def decode(words):
#     for vowel in vowels:
#         words = words.replace(vowel + 'p' + vowel, vowel)
#     return words


# for line in sys.stdin:
#     words = line.strip().split()
#     print(decode(' '.join(words)))