def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] if l[0] < maximum(l[1:]) else maximum(l[1:])
    




# def minimum(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if nums[0] < nums[1]:
#         del(nums[1])
#     else:
#         del(nums[0])
#     return (minimum(nums))