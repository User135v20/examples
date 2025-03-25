"""
The input is a sorted array.
The output should be a sorted array of squares.
"""

from array import *
from sortedcontainers import SortedList

input_array = array('i', [-11, 2, 3, 4, 5])
# first

result = SortedList()
for el in input_array:
    result.add(el * el)
result = array('i', result)
print(array('i', result))

# second
result_v2 = [0] * len(input_array)
right = len(input_array) - 1
left = 0
for i in range(len(result_v2) - 1, -1, -1):
    if abs(input_array[right]) > abs(input_array[left]):
        result_v2[i] = input_array[right] ** 2
        right -= 1
    else:
        result_v2[i] = input_array[left] ** 2
        left += 1
print(array('i', result_v2))
