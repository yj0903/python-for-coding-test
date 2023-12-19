# boj 11286 절댓값 힙
# 난이도 실버1

import sys
import heapq
n = int(sys.stdin.readline())
heap = []

for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            i, j = heapq.heappop(heap)
            print(j)
    else:
        heapq.heappush(heap, [abs(m), m])

