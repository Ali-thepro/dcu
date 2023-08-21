import sys
import string

seen = []

for line in sys.stdin.readlines():
    line = line.strip().split()
    output = []
    for word in line:
        word = word.lower().strip(string.punctuation)
        if word not in seen:
            seen.append(word)
            output.append(word)
        else:
            output.append('.')
    print(' '.join(output))




# seen = set()
# for line in sys.stdin:
#     output = []
#     line = line.strip().split()
#     for word in line:
#         word = word.lower().strip(string.punctuation)
#         if word in seen:
#             output.append('.')
#         else:
#             output.append(word)
#         seen.add(word)
#     print(' '.join(output))




# import sys
# import string


# word_set = set()
# def nodups(words):
#     for index, word in enumerate(words):
#         if word[-1] in string.punctuation:
#             word = word[:-1]
#         if word.lower() in word_set:
#             words[index] = '.'
#         else:
#             word_set.add(word.lower())
#     return ' '.join(words)


# for line in sys.stdin:
#     words = line.strip().split()
#     print(nodups(words))





# import sys
# import string

# seen = []

# for line in sys.stdin.readlines():
#     line = line.strip().split()
#     i = 0
#     for word in line:
#         word = word.lower().strip(string.punctuation)
#         if word not in seen:
#             seen.append(word)
#         else:
#             line[i] = '.'
#         i += 1
#     print(' '.join(line))





# import sys
# import string


# word_list = []
# def nodups(words):
#     for index, word in enumerate(words):
#         word = word.lower().strip(string.punctuation)
#         if word in word_list:
#             words[index] = '.'
#         else:
#             word_list.append(word)


#     return ' '.join(words)


# for line in sys.stdin:
#     words = line.strip().split()
#     print(nodups(words))





# import sys
# import string

# seen = []

# for line in sys.stdin:
#     line = line.strip().split()
#     for index, word in enumerate(line):
#         word = word.lower().strip(string.punctuation)
#         if word in seen:
#             line[index] = '.'
#         else:
#             seen.append(word)
#     print(' '.join(line))