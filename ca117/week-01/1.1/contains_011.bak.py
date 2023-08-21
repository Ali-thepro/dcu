import sys

for word in sys.stdin:
    words = word.split()
    words[0] = words[0].lower()
    words[1] = words[1].lower()
    new_word = words[1]

    for letter in words[0]:
        if letter in words[1]:
            new_word = new_word.replace(letter, "")

    if len(new_word) == len(words[1]) - len(words[0]):
        print(True)
    else:
        print(False)




# import sys

# def contains(word1, word2, letterList=[]):
#     word1, word2 = word1.lower(), word2.lower()
#     letterList = [l for l in word1 if l in word2 and word1.count(l) == 1]
#     return len(letterList) == len(word1)
  
# def main():
#     for data in sys.stdin:
#         first, second = data.strip().split()
#         print(contains(first, second))

# if __name__ == "__main__":
#     main()




# import sys
# for line in sys.stdin:
#     lines = line.strip().split()
#     part = lines[0].lower()
#     full = lines[1].lower()
#     count = 0
#     seen = []
#     for letter in part:
#         if letter not in seen:
#             seen.append(letter)
#             if letter in full:
#                 count += 1
#     print(count == len(part))





# import sys
# lines = sys.stdin.readlines()

# for line in lines:
#     words = line.lower().split()
#     check = words[0].strip()
#     for s in words[1]:
#         check = check.replace(s, "", 1)
#     if len(check) > 0:
#         print("False")
#     else:
#         print("True")