import sys

for line in sys.stdin:
    x, y = line.split()
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    elif x > 0 and y < 0:
        print("4")
    else:
        print("0")
