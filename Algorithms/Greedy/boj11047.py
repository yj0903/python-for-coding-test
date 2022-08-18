# boj11047 동전 O
# 실버4

# 메모리 30840 KB
# 시간 68 ms

import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(n)]
count = 0

for coin in coin_list[::-1]:
    if k >= coin:
        count += k//coin
        k = k % coin

print(count)