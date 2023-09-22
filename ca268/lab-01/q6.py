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