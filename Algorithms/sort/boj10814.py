# boj10814 나이순정렬
# 난이도 실버5

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    arr.append([age, name])

arr.sort(key=lambda x: int(x[0]))
print('\n'.join(' '.join(a) for a in arr))
