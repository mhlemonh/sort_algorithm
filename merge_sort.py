#!/usr/bin/env python
import numpy as np

def merge_sort(list_to_sort):
    if len(list_to_sort)<2:
        return list_to_sort
    else:
        middle_point = len(list_to_sort)//2
        return merge(merge_sort(list_to_sort[:middle_point]),merge_sort(list_to_sort[middle_point:]))

def merge(a_list, b_list):
    a_i, b_i = 0, 0
    meet_list_end = False
    merged_list = []
    while not meet_list_end:
        try:
            if a_list[a_i] >= b_list[b_i]:
                merged_list.append(b_list[b_i])
                b_i += 1
            else:
                merged_list.append(a_list[a_i])
                a_i += 1
        except:
            if a_i < len(a_list):
                merged_list.extend(a_list[a_i:])
            else:
                merged_list.extend(b_list[b_i:])
            meet_list_end = True
    return merged_list

if __name__ == '__main__':
    #np.random.seed(9487)
    range_min, range_max = 0, 100
    l1=np.random.randint(range_min, range_max, size=9).tolist()
    l2=np.random.randint(range_min, range_max, size=9).tolist()
    l1.sort()
    l2.sort()
    print "Initial list1:", l1
    print "Initial list2:", l2
    sl = merge(l1, l2)
    print " Sorted list:", sl
