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
import math


# solution 1
# Create a dictionary where the key is a number and the value is a list of decimal numbers with that many number of 1's
# in their binary representation. Iterate through the input list to add numbers to the dictionary. To build the
# sorted list, sort the keys of the dictionary from least to greatest and sort each individual list of numbers from
# least to greatest and append them in that order.


def rearrange(elements: List[int]) -> List:
    dict = {}  # key: number of 1's in binary representation, value: list of numbers with that many number of 1's
    for e in elements:
        num_of_ones = bin(e).count("1")
        if num_of_ones not in dict:
            dict[num_of_ones] = [e]
        else:
            dict[num_of_ones].append(e)

    sorted_list = []

    ls = list(dict.keys())
    ls.sort()
    print("List sorted: ", ls)
    for key in ls:
        sorted_list.extend(sorted(dict[key]))

    return sorted_list


print(rearrange([7, 8, 6, 5]))  # 8, 5, 6, 7
print(rearrange([1, 2, 3]))  # 1, 2, 3
print(rearrange([3, 2, 1]))  # 1, 2, 3

list0 = list(range(9))
list1 = list(reversed(list0))
print(list0, list1)

print(rearrange(list0))  # 0, 1, 2, 4, 8, 3, 5, 6, 7
print(rearrange(list1))  # 0, 1, 2, 4, 8, 3, 5, 6, 7


# solution 2
# Use the built-in sorting function. To sort a list based on multiple attributes, sort the keys on the secondary
# attribute and then on the primary attribute (sort by decimal value and then sort by number of 1's in the binary
# representation). See: https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
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
# Like the last method, but instead of calling sort twice let's try to sort them all in one line. To do this the key
# which sort is based on will need to encode both the number of 1's in the binary representation and the decimal value
# of the number. We can fit both in one number by giving them separate portions of that number.

# example:
# The number 12 ('1100' in binary) has two 1's and a value of 12, so we could encode it as the number 2........12 with
# some amount of space ... in between

# Because element[i] can be up to 10^9, we need up to 9 digits for the right portion. In order to prevent the part that
# encodes the number of 1's from overlapping with the part that encodes the decimal value, we need to multiply the number
# of 1's by 10^9. The number of 1's can be at most 29 (math.log2(1e9) = 29.89) so our key can be at most 10 digits long.
print()


def rearrange(elements: List[int]) -> List:
    return sorted(elements, key=lambda x: (bin(x).count("1") * 10**9) + x)


print(rearrange([7, 8, 6, 5]))  # 8, 5, 6, 7
print(rearrange([1, 2, 3]))  # 1, 2, 3
print(rearrange([3, 2, 1]))  # 1, 2, 3
print(rearrange(list0))  # 0, 1, 2, 4, 8, 3, 5, 6, 7
print(rearrange(list1))  # 0, 1, 2, 4, 8, 3, 5, 6, 7


# Extra: sort the integers of a list by the their value if you were put a decimal at the start of the number

# example:
#  1 -> 0.1
#  5 -> 0.5
# 13 -> 0.13
# so [1, 5, 13] becomes [1, 13, 5]


nums = [57, 11, 71, 6, 20, 51, 64, 36, 37, 65, 86, 4, 20, 60, 17, 59, 99, 78, 63, 8, 19, 95, 23, 3, 58]
nums100 = list(range(1, 101))

# solution
# math.log10(x) gives the number of digits in an integer 'x' minus 1, so int(math.log(x) + 1) gives the total number
# of digits. Divide the number x by 10**(number of digits it has) to move it all to the right of the decimal point.

print(sorted(nums, key=lambda x: x / 10**(int(math.log10(x) + 1))))
print(sorted(nums100, key=lambda x: x / 10**(int(math.log10(x) + 1))))
