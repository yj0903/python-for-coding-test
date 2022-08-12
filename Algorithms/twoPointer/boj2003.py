# boj2003 수들의 합2
# 난이도 실버4

# 메모리 30840 KB
# 시간 588 ms

import sys

n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 1
count = 0

while left <= right <= n:
    total = sum(arr[left:right])
    if total < target:
        right += 1
    elif total > target:
        left += 1
    elif total == target:
        count += 1
        left += 1
print(count)