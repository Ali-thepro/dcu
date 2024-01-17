def reverse(l):
    if l == []:
        return []
    else:
        return [l[-1]] + reverse(l[:-1])
        #return reverse(l[1:]) + [l[0]]
