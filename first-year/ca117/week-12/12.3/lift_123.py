import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())

count = 0
while s != g:
    if s < g:
        if u > 0:
            s += u
            count += 1
        else:
            print('Sorry Sheila!')
            break

    elif s > g:
        if d > 0:
            s -= d
            count += 1
        else:
            print('Sorry Sheila!')
            break

if s == g:
    print(count)