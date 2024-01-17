import sys

number = sys.stdin.readline().strip()

def magicnumber(n):
    magic_number = ""
    while n > 0:
        if n % 2 == 0:
            magic_number += "9"
        else:
            magic_number += "3"
        n = (n - 1) // 2
    return int(magic_number[::-1])

n = int(number)
print(magicnumber(n))