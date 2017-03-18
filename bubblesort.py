#!/usr/bin/env python
"""
A practice of sorting algorithm
"""

def bubble_sort(list_to_sort):
    for j in range(len(list_to_sort)-1,0,-1):
        for i in range(j):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i+1], list_to_sort[i] = list_to_sort[i], list_to_sort[i+1]
    return list_to_sort

def bubble_sort_02(list_to_sort):
    ll = len(list_to_sort)-1
    index_flow = [ j for i in range(ll,0,-1) for j in range(i)]
    for i in index_flow:
        if list_to_sort[i] > list_to_sort[i+1]:
            list_to_sort[i+1], list_to_sort[i] = list_to_sort[i], list_to_sort[i+1]
    return list_to_sort


if __name__ == '__main__':
    list_to_sort = [5,1,7,4,6,2,9,3,8]
    print bubble_sort(list_to_sort)
    list_to_sort = [5,1,7,4,6,2,9,3,8]
    print bubble_sort_02(list_to_sort)
