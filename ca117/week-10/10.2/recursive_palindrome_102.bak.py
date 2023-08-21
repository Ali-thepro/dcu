def rpal(s):
    if s == '':
        return True
    else:
        return s[0] == s[-1] and rpal(s[1:-1])