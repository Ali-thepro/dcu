def move_vow(line):

    vowels = 'aeiouAEIOU'
    a = []
    for ch in line:
        if ch in vowels:
            a.append(ch)
    
    for ch in line:
        if ch not in vowels:
            a.append(ch)
    return ''.join(a)

print(move_vow('This is DCU!'))