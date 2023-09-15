def filter_star(d, num):
    result = {}
    for key, value in d.items():
        if len(value) == num:
            result[key] = value
    if len(result) == 0:
        return "No result found!"
    else:
        return result
    

print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 4))


# def filter_star(the_dict, nr_stars):
#     new_dict = {}
#     for x in the_dict:
#         if len(the_dict[x]) == nr_stars:
#             new_dict[x] = '*' * nr_stars
#     if len(new_dict) == 0:
#         return 'No result found!'
#     else:
#         return new_dict