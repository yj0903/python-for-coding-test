# boj11004 K번째 수
# 난이도 실버5

# 메모리 622580 KB
# 시간 3872 ms

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
print(arr[k-1])
