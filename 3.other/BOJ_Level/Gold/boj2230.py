# boj2230 수 고르기
# 골드5

# 메모리 32888 KB
# 시간 152 ms

import sys

n, m = map(int, sys.stdin.readline().split())

# 중복제거 set 집합
arr = set()
for _ in range(n):
    arr.add(int(sys.stdin.readline().strip()))

# 투포인터 쓰려면 정렬 필요.
arr = sorted(list(arr))

# 최댓값을 sys.maxsize 이렇게 표현 ** 이것 때문에 계속 틀림
left, right, diff = 0, 1, sys.maxsize
while left != len(arr):
    d = arr[right] - arr[left]
    if d > m:
        diff = min(diff, d)
        left += 1
    elif d == m:
        diff = d
        break
    else:
        if right == len(arr)-1:
            left += 1
        else:
            right += 1
print(diff)