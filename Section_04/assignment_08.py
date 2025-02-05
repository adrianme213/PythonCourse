# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:
def sum78(my_list):
    if len(my_list) == 0:
        return 0

    new_list = []
    ii = 0
    while ii < len(my_list):
        if my_list[ii] == 7:
            while my_list[ii] != 8:
                ii += 1
        else:
            new_list.append(my_list[ii])
        ii += 1

    return sum(new_list)

print(sum78([1,2,2]) == 5)
print(sum78([1,2,2,7,99,99,8]) == 5)
print(sum78([1,1,7,8,2]) == 4)
print(sum78([]) == 0)
print(sum78([1]) == 1)

























# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum