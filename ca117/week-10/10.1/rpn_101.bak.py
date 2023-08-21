from math import sqrt

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
    
def isDigit(n):  # improved isdigit function that handles floats
    try:
        float(n)
        return True
    except ValueError:
        return False
    

def calculator(line):

    binops = {'+': float.__add__,
            '-': float.__sub__,
            '*': float.__mul__,
            '/': float.__truediv__}
    
    uniops = {'n': float.__neg__,
          'r': sqrt}
    
    s = Stack()


    for ch in line.split():
        if isDigit(ch):
            s.push(float(ch))
        elif ch in binops:
            n2 = s.pop()
            n1 = s.pop()
            s.push(binops[ch](n1, n2))
        elif ch in uniops:
            s.push(uniops[ch](s.pop()))
        # else:
        #     s.push(float(ch))

    return s.pop()
#     #return s.top()





# def calculator(test):
#    binops = {'+': float.__add__, '-': float.__sub__,
#              '*': float.__mul__, '/': float.__truediv__}
#    uniops = {'n': float.__neg__, 'r': sqrt}
#    ops = '+-*/nr'
#    s = Stack()
#    for c in test.split():
#       if c not in ops:
#          s.push(float(c))
#       elif c in binops:
#          second, first = s.pop(), s.pop()
#          s.push(binops[c](first, second))
#       elif c in uniops:
#          s.push(uniops[c](s.pop()))
#    return s.top()







# binops = {'+': float.__add__,
#           '-': float.__sub__,
#           '*': float.__mul__,
#           '/': float.__truediv__}

# uniops = {'n': float.__neg__,
#           'r': sqrt}


# def calculator(chars):

#     s = Stack()
#     for c in chars.split():
#         try:
#             s.push(float(c))

#         except ValueError:
#             if s.is_empty() is False:
#                 if c in binops.keys():
#                     last = s.pop()
#                     suma = binops[c](s.pop(), last)
#                     s.push(suma)
#                 elif c in uniops.keys():
#                     suma = uniops[c](s.pop())
#                     s.push(suma)

#     return s.top()











