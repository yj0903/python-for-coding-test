# boj1931 회의실 배정
# 실버1

# 메모리 57760 KB
# 시간 300 ms

import sys

n = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 그리디하게 생각해보면,
# 회의 수가 많으려면 회의종료시점이 작을수록 좋다.
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
now = 0

for start, end in meetings:
    if now <= start:
        count += 1
        now = end
print(count)