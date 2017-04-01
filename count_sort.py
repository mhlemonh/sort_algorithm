#!/usr/bin/env python
import numpy as np

"""
The count sort is only used in integer list sorting.
"""

def count_sort(list_to_sort, min_value, max_value):
    count_list=[0 for i in xrange(min_value, max_value)]
    sorted_list=[0 for i in xrange(len(list_to_sort))]
    for value in list_to_sort:
        count_list[value] += 1
    for i in xrange(min_value+1, max_value):
        count_list[i] = count_list[i] + count_list[i-1]
    for j in reversed(xrange(len(list_to_sort))):
        list_value = list_to_sort[j]
        sorted_list[count_list[list_value]-1] = list_value
        count_list[list_value] -= 1
    return sorted_list
    
if __name__ == '__main__':
    np.random.seed(9487)
    range_min, range_max = 0, 100
    l=np.random.randint(range_min, range_max, size=10).tolist()
    print "Initial list:", l
    sl = count_sort(l,range_min, range_max)
    print " Sorted list:", sl
