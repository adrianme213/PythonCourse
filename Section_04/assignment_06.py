# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

# Your Code Below:
def last2(my_str):
    if len(my_str) <= 2:
        return 0
    one, two = my_str[-2], my_str[-1]

    ii = 0
    result = 0
    while ii < len(my_str)-2:
        if (my_str[ii] == one) and (my_str[ii+1] == two):
            result += 1
        ii += 1

    return result

print(last2('hixxhi')) #→ 1
print(last2('xaxxaxaxx')) #→ 1
print(last2('axxxxaaxx')) #→ 3
print(last2('xxx')) #→ 1




























# Solution

# def last2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count
