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
    for i in range(iter_time):
        bucket = [[] for j in range(base)]
        for item in merged_bucket:
            bucket_number = (item // (base**i)) % base
            bucket[bucket_number].append(item)
        merged_bucket = sum(bucket, [])
    return merged_bucket

if __name__ == '__main__':
    range_min, range_max = 0, 300
    np.random.seed(9487)
    l=np.random.randint(range_min, range_max, size=10).tolist()
    print "Initial list:", l
    sl = radix_sort(l, 2)
    print " Sorted list:", sl
