# boj1655 가운데를 말해요
# 난이도 골드2

import sys
import heapq

n = int(sys.stdin.readline())
left_heap = []
right_heap = []

for i in range(n):
    m = int(sys.stdin.readline())
    if len(left_heap) <= len(right_heap):
        heapq.heappush(left_heap, (-m, m))
    else:
        heapq.heappush(right_heap, (m, m))

    if len(left_heap) != 0 and len(right_heap) != 0:
        if left_heap[0][1] > right_heap[0][1]:
            l_idx, l_val = heapq.heappop(left_heap)
            r_idx, r_val = heapq.heappop(right_heap)
            heapq.heappush(left_heap, (-r_idx, r_val))
            heapq.heappush(right_heap, (-l_idx, l_val))
    print(left_heap[0][1])
