#!/usr/bin/env python
import numpy as np
from math import log
def max_redix(list_to_sort, base=10):
    try:
        return int(log(max(list_to_sort), base)) + 1
    except ValueError:
        return 1
def radix_sort(list_to_sort, base=10):
    iter_time = max_redix(list_to_sort, base)
    merged_bucket = list_to_sort
    bucket = [[] for i in range(base)]
    for i in range(iter_time):
        for item in merged_bucket:
            bucket_number = item // (base**i)
            bucket[bucket_number].append(item)

        merged_bucket = reduce(apend)
    return sorted_list

if __name__ == '__main__':
    range_min, range_max = 0, 300
    l=np.random.randint(range_min, range_max, size=9).tolist()
    print "Initial list:", l
    print max_redix(l, 2)
    #sl = radix_sort(l)
    #print " Sorted list:", sl
