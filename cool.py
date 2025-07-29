"""
Find kth min or max element in the array
"""

import heapq
from typing import List

def find_kth_min_max(arr: List, k: int):
    min_heap = []
    for el in arr:
        heapq.heappush(min_heap, el)

    kth_min_el = None
    for i in range(k):
        kth_min_el = heapq.heappop(min_heap)

    max_heap = []
    for el in arr:
        heapq.heappush(max_heap, -el)

    kth_max_el = None
    for i in range(k):
        kth_max_el = -heapq.heappop(max_heap)

    return (kth_max_el, kth_min_el)

kth_max, kth_min = find_kth_min_max([3,2,1,5,6,4], 2)
print("kth_max", kth_max)
print("kth_min", kth_min)