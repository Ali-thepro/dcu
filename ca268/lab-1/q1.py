def q1_sum(num_list):
    total = 0
    for row in num_list:
        try:
            if row % 2 == 0:
                total += row
        except TypeError:
            for num in row:
                if num % 2 == 0:
                    total += num
    return total

print(q1_sum([1,2,4]))
