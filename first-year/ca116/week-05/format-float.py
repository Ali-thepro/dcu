#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and s[i] != ".":
    i = i + 1

if i == 0:
  print("0" + s)
elif i == len(s):
  print(s + ".0")
elif s[len(s) - 1] == ".":
  print(s + "0")
elif s[0] == "-" and s[1] == ".":
  print("-" + "0" + s[1:len(s)])
else:
  print(s)




#ogyammers
#!/usr/bin/env python3

# s = input()

# i = 0
# while i < len(s) and s[i] != ".":
#    i = i + 1

# if s[(len(s) - 1)] == ".":
#    print(s + "0")
# elif i == len(s):
#    print(s + ".0")
# elif s[0] == ".":
#    print("0" + s)
# elif s[0] == "-" and s[1] == ".":
#    print("-0" + s[1:])
# elif s[(len(s) - 1)] == ".":
#    print(s + "0")
# else:
#    print(s)




#ssdrum
#!/usr/bin/env python3

# s = input()

# i = 0
# while i < len(s) and s[i] != ".":
#     i = i + 1
# if i == 0:
#     print("0" + s)
# elif i == len(s):
#     print(s + ".0")
# elif i == len(s) - 1:
#     print(s + "0")
# elif s[0] == "-" and s[1] == ".":
#     print(s[:1] + "0" + s[1:])
# else:
#     print(s)




#!/usr/bin/env python3

# s = input()

# i = 0
# while i < len(s) and s[i] != ".":
#   i += 1

# if i == len(s):
#   print(s + ".0")
# elif s[0] == ".":
#   print("0" + s)
# elif s[1] == "." and s[0] == "-":
#   print(s[0] + "0" + s[1:len(s)])
# elif s[len(s) - 1] == ".":
#   print(s + "0")
# else:
#   print(s)