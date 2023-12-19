# boj11279 최대힙
# 난이도 실버2

import sys
import heapq
n = int(sys.stdin.readline())

# 방법1) heapq 라이브러리 사용
que = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m != 0:
        heapq.heappush(que, m*(-1))
    else:
        if len(que) == 0:
            print(0)
        else:
            print(heapq.heappop(que)*(-1))


# 방법2) 라이브러리 없이 최대힙 구현



