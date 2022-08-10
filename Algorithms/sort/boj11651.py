# boj11651 좌표정렬하기2
# 난이도 실버5

# 메모리 54448 KB
# 시간 404 ms

import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr = sorted(arr, key=lambda a: (a[1], a[0]))
for x, y in arr:
    print(x, y)