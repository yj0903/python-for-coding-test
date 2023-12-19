# boj2003 수들의 합2
# 난이도 실버4

# 메모리 30840 KB
# 시간 76 ms

# chsun0303(13437875)

import sys

n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, total, count = 0, 0, 0

for i in arr:
    total += i
    while total > target:
        total -= arr[left]
        left += 1
    count += (total == target)
print(count)