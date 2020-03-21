"""
# Ascending Binary Sort

Consider an array of decimal integers. Rearrange the array according to the following rules:

- Sort the integers in ascending order by the number of 1's in their binary representation
- Elements having the same number of 1's in their binary are ordered by increasing decimal value.

### Example
Consider the array [7, 8, 6, 5] = [0111, 1000, 0110, 0101]. First, group the items by number of binary digits equal to 1: [[1000], [[0101], [0110]], [0111]]. The elements with two 1's now must be ordered:
[0110, 0101] = [6,5]. Sort those two elements in ascending order by value making the final array [1000, 0101, 0110, 0111] = [8, 5, 6, 7]

#### Function Description
Complete the function rearrange in the editor below:

rearrange has the following parameter(s):
    *int elements[n]:* an array of integers to sort

Returns:
    *int[n]* an array of decimal integers sorted per the given rules

### Constraints
- 1 <= n <= 10^5
- 1 <= elements[i] <= 10^9
"""
from typing import *

def rearrange(elements: List[int]) -> List:
    dict = {}  # number to list of numbers
    for e in elements:
        numOnes = bin(e).count("1")
        if numOnes not in dict:
            dict[numOnes] = [e]
        else:
            dict[numOnes].append(e)

    sortedList = []

    ls = list(dict.keys())
    ls.sort()
    for key in ls:
        sortedList.extend(sorted(dict[key]))

    return sortedList

# print(bin(7), bin(7).count("1"))

print(rearrange([7, 8, 6, 5]))  # 8, 5, 6, 7
print(rearrange([1, 2, 3]))  # 1, 2, 3
print(rearrange([3, 2, 1]))  # 1, 2, 3

list0 = list(range(9))
list1 = list(reversed(list0))
print(list0, list1)

print(rearrange(list0))  # 0, 1, 2, 4, 8, 3, 5, 6, 7
print(rearrange(list1))  # 0, 1, 2, 4, 8, 3, 5, 6, 7

import random
import math


# solution 2
print()
def rearrange(elements: List[int]) -> List:
    elements.sort()
    elements.sort(key=lambda num: bin(num).count("1"))
    return elements


print(rearrange([7, 8, 6, 5]))  # 8, 5, 6, 7
print(rearrange([1, 2, 3]))  # 1, 2, 3
print(rearrange([3, 2, 1]))  # 1, 2, 3
print(rearrange(list0))  # 0, 1, 2, 4, 8, 3, 5, 6, 7
print(rearrange(list1))  # 0, 1, 2, 4, 8, 3, 5, 6, 7

# solution 3
# number of 1's ... decimal value
print()
def rearrange(elements: List[int]) -> List:
    return sorted(elements, key=lambda x: bin(x).count("1") * 10**5 + x**0.5)


print(rearrange([7, 8, 6, 5]))  # 8, 5, 6, 7
print(rearrange([1, 2, 3]))  # 1, 2, 3
print(rearrange([3, 2, 1]))  # 1, 2, 3
print(rearrange(list0))  # 0, 1, 2, 4, 8, 3, 5, 6, 7
print(rearrange(list1))  # 0, 1, 2, 4, 8, 3, 5, 6, 7

nums = [57, 11, 71, 6, 20, 51, 64, 36, 37, 65, 86, 4, 20, 60, 17, 59, 99, 78, 63, 8, 19, 95, 23, 3, 58]
print(sorted(nums, key=lambda x: x / 10**(int(math.log10(x) + 1))))


