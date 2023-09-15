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





# def move_vow(line):
#     vow = 'aeiouAEIOU'
#     final_vow = ''
#     final_cos = ''
#     for x in line:
#         if x in vow:
#             final_vow += x
#         else:
#             final_cos += x
#     final = final_vow + final_cos
    
#     return final
# print(move_vow('This is DCU!'))


# def move_vow(line):
#     vowels = 'aeiouAEIOU'
#     vow = []
#     con = []
#     for ch in line:
#         if ch in vowels:
#             vow.append(ch)
#         else:
#             con.append(ch)
#     return ''.join(vow + con)

# print(move_vow('This is DCU!'))
