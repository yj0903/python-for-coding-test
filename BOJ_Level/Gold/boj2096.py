# boj2096 내려가기
# 골드5

# 메모리 115176 KB
# 시간 196 ms

import sys

num = int(sys.stdin.readline())
min_arr = [0, 0, 0]
max_arr = [0, 0, 0]

for i in range(num):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    min_arr = [a + min(min_arr[:2]), b + min(min_arr), c + min(min_arr[1:])]
    max_arr = [a + max(max_arr[:2]), b + max(max_arr), c + max(max_arr[1:])]

print(max(max_arr), min(min_arr))




