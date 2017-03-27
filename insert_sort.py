#!/usr/bin/env python

def insert_sort(list_to_sort):
    finished_list = []
    index = binary_search(list_to_sort)

def binary_search(sorted_list, value):
    """ Return the index just smaller than the value."""
    end = len(sorted_list)-1
    start = 0
    search_done = False
    for i in range(7):
    #while not search_done:
        mid = (end+start)/2
        print start, mid, end
        if sorted_list[mid] == value:
            print 'A'
            return mid-1
        elif start == end:
            return mid-1
        elif sorted_list[mid] < value and sorted_list[mid+1] < value:
            print 'B'
            start = mid
        elif value < sorted_list[mid] and value < sorted_list[mid+1]:
            print 'C'
            end = mid
        else:
            return mid
    return mid
if __name__ == '__main__':
    list_to_sort = [5,1,7,4,6,2,9,3,8]
    sl = [1,2,3,4,5,6,7,8,9,10]
    print binary_search(sl,-100)
    #insert_sort()
