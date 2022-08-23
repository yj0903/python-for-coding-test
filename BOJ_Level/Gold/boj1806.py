# boj1806 부분합
# 골드4
# 유사 문제: boj1644 소수의 연속합

# 메모리
# 시간
import sys

n, s = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().strip().split()))
sum_arr = [0] * (n + 1)
for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

left, right, result = 0, 1, 100000
while left != n:
    if sum_arr[right] - sum_arr[left] >= s:
        if right-left < result:
            result = right-left
        left += 1
    else:
        if right == n:
            left += 1
        else:
            right += 1

if result == 100000:
    print(0)
else:
    print(result)