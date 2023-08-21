
import sys

h1, h2, h3, h4, h5, h6, h7, h8, h9, h10 = 'POS', 'CLUB', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'

leagues = [line.strip().split() for line in sys.stdin]


clubs = [" ".join(line[1:-8]) for line in leagues]
length = (len(max(clubs, key=len)))

print(f'{h1:>3s} {h2:{length:d}s} {h3:>2s} {h4:>3s} {h5:>3s} {h6:>3s} {h7:>3s} {h8:>3s} {h9:>3s} {h10:>3s}')


for line in leagues:
    pos = line[0]
    club = " ".join(line[1:-8])
    p = (line[-8])
    w = line[-7]
    d = line[-6]
    l = line[-5]
    gf = line[-4]
    ga = line[-3]
    gd = line[-2]
    pts = line[-1]

    print(f'{pos:>3s} {club:{length:d}s} {p:>2s} {w:>3s} {d:>3s} {l:>3s} {gf:>3s} {ga:>3s} {gd:>3s} {pts:>3s}')





#!/usr/bin/env python3

# import sys
# h1, h2, h3, h4, h5, h6, h7, h8, h9, h10 = 'POS', 'CLUB', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'

# lines = []
# for line in sys.stdin:
#     lines.append(line.strip().split())

# clubs = []
# for line in lines:
#     clubs.append(' '.join(line[1:-8]))

# max_width = 0
# for club in clubs:
#     if len(club) > max_width:
#         max_width = len(club)

# print(
#     f'{h1:>3s} {h2:{max_width:d}s} {h3:>2s} {h4:>3s} '
#     f'{h5:>3s} {h6:>3s} {h7:>3s} {h8:>3s} {h9:>3s} {h10:>3s}')

# for line in lines:
#     pos = int(line[0])
#     club = ' '.join(line[1:-8])
#     played = int(line[-8])
#     won = int(line[-7])
#     drawn = int(line[-6])
#     lost = int(line[-5])
#     gf = int(line[-4])
#     ga = int(line[-3])
#     gd = int(line[-2])
#     pts = int(line[-1])
#     print(
#         f'{pos:3d} {club:{max_width:d}s} {played:2d} {won:3d} '
#         f'{drawn:3d} {lost:3d} {gf:3d} {ga:3d} {gd:3d} {pts:3d}')





#!/usr/bin/env python3

# import sys
# pos, clubs, p, w, d, l, gf, ga, gd, pts = ['POS'], ['CLUB'], ['P'], ['W'], ['D'], ['L'], ['GF'], ['GA'], ['GD'], ['PTS']
# longest = ''

# for line in sys.stdin:
#     line = line.split()
#     pos.append(line[0])
#     line = line[1:]
#     i = 0
#     while i < len(line) and not line[i].isnumeric():
#         i += 1
#     p.append(line[i])
#     w.append(line[i+1])
#     d.append(line[i+2])
#     l.append(line[i+3])
#     gf.append(line[i+4])
#     ga.append(line[i+5])
#     gd.append(line[i+6])
#     pts.append(line[i+7])
#     club = ' '.join(line[:i])
#     clubs.append(club)
#     if len(club) > len(longest):
#         longest = club

# for i in range(len(pos)):
#     print(f'{pos[i]:>3s} {clubs[i]:{len(longest)}s} {p[i]:>2s} {w[i]:>3s} {d[i]:>3s} {l[i]:>3s} {gf[i]:>3s} {ga[i]:>3s} {gd[i]:>3s} {pts[i]:>3s}')
    




#!/usr/bin/env python3

# import sys
# clubs = []
# remain = []

# for line in sys.stdin:
#   line = line.strip()
#   i = 0
#   while i < len(line) and not line[i].isalpha():
#     i = i + 1
#   j = i
#   while j < len(line) and (line[j].isalpha() or line[j] == " " or line[j] == "&"):
#     j = j + 1
#   clubs.append(line[i:j])
#   remain.append(line[j:])

# clublen = len(max(clubs, key=len))

# print("POS CLUB" + " " * (clublen - 3) + "P   W   D   L  GF  GA  GD PTS")
# pos = 1

# for i in range(len(clubs)):
#   tokens = remain[i].split()
#   print(f"{pos:3d}" + " " + f"{clubs[i]:{clublen}s}" + f"{tokens[0]:3s} " + f"{tokens[1]:>2s}  " + f"{tokens[2]:>2s}  " + f"{tokens[3]:>2s}  " + f"{tokens[4]:>2s}  " + f"{tokens[5]:>2s} " + f"{tokens[6]:>3s} " + f"{tokens[7]:>3s}")
#   pos = pos + 1

