# boj2075 N번째 큰수
# 난이도 실버2

# 메모리 119352 KB
# 시간 1072 ms

import sys

n = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))
result.sort()

for i in range(n-1):
    arr = list(map(int, sys.stdin.readline().split()))

    for a in arr:
        if a > result[0]:
            result[0] = a
            result.sort()

print(result[0])