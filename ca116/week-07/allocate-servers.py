#!/usr/bin/env python3

servers = []
s = input()
while s != "end":
    start = int(s)
    i = 0
    while i < len(servers) and not (servers[i] <= start):
        i = i + 1

    if i < len(servers):
        servers[i] = start + 1000
    else:
        servers.append(start + 1000)

    s = input()
print(len(servers))




# tot_num_serv = 0
# jobs = []

# start_time = input()
# while start_time != "end":
#     jobs.append(int(start_time))
#     curr_used_serv = 0

#     i = 0
#     while i < len(jobs):
#         if int(start_time) <= jobs[i] + 1000:
#             curr_used_serv = curr_used_serv + 1
#             if tot_num_serv < curr_used_serv:
#                 tot_num_serv = curr_used_serv
#         i = i + 1
#     start_time = input()

# print(tot_num_serv)




#!/usr/bin/env python3

# a = []
# s = input()
# while s != 'end':
#     a.append(int(s))
#     s = input()

# i = 0
# x = 0
# while i < len(a):
#     j = 1
#     while i + j < len(a) and a[i + j] - a[i] < 1001:
#         j += 1
#     if j > x:
#         x = j
#     i += 1
# print(x)
