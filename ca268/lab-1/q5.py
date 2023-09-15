def histogram(num_list, char):

    for num in num_list:
        print(char * num)

histogram([6, 200], '=')



# def histogram(line, type):
#     final = [''] * len(line)
#     for i, x in enumerate(line):
#         final[i] = (type * x)
#         print(final[i])
# histogram([6, 2, 15 , 3, 20 , 5], '=')


# def histogram(a,type):
#     res = ""
#     for i in a:
#         res += type * i
#         res += "\n"
#     print(res)
# histogram([6, 2, 15 , 3, 20 , 5], '=')