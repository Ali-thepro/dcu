class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        if len(self) > 0:
            return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)


def matcher(line):
    d = {')': '(',
     '}': '{',
     ']': '['}

    s = Stack()
    for c in line:
        if c in d.values():
            s.push(c)

        else:
            if d[c] != s.pop():
                return False
    return s.is_empty()


# def matcher(test):
#     d = {')': '(', ']': '[', '}': '{'}
#     if test[0] not in d.keys():
#         return False

#     s = Stack()
#     for c in test:
#         if c in d.values():
#             s.push(c)
#         elif c in d.keys() and d[c] == s.top():
#             s.pop()
#         elif c in d.keys() and d[c] != s.top():
#             return False
#     return s.is_empty()





# def matcher(s):
#     pairs = {")": "(", "]": "[", "}": "{"}
#     tokens = Stack()

#     for c in s:
#         if c in pairs.values():  # add char to stack if is an opening bracket
#             tokens.push(c)
#         elif c in pairs:
#             try:  # avoids indexerror if first char is a closing bracket
#                 if tokens.pop() != pairs[c]:  # check if popped bracket corresponds to correct closing bracket
#                     return False
#             except IndexError:
#                 return False




# def matcher(test):
#    d = {')': '(', ']': '[', '}': '{'}
#    lefties, righties = '([{', ')]}'
#    if test[0] not in lefties:
#      return False

#    s = Stack()
#    for c in test:
#       if c in lefties:
#          s.push(c)
#       if c in righties:
#          if d[c] != s.top():
#             return False
#          s.pop()
#    return len(s) == 0




# d = {')': '(', '}': '{', ']': '['}
# def matcher(line):

#     s = Stack()

#     for c in line:

#         if c in d.values():
#             s.push(c)

#         elif c in d.keys():
#             if d[c] != s.pop():
#                 return False

#     return s.is_empty()


#------------------------------------------------------------------------------------

#doesnt work with stack object

# def matcher(line):
    # line = list(line)
    # d = {')': '(',
    #  '}': '{',
    #  ']': '['}

    # check = []
    # if line[0] in d:
    #     check.append(line)
    # for c in line:
    #     if c in d.values():
    #         check.append(c)
    #     elif c in d.keys():
    #         if len(check) > 0 and d[c] == check[-1]:
    #             check.pop()
    # return len(check) == 0


# def matcher(line):
    # d = {')': '(',
    #  '}': '{',
    #  ']': '['}

    # stack = []
    # for c in line:
    #     if c in d:
    #         if stack and stack[-1] is d[c]:
    #             stack.pop()
    #         else:
    #             return False   
    #     else:
    #         stack.append(c)

    # return True if not stack else False