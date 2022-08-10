# boj18870 좌표압축
# 난이도 실버2
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = []
for y in arr:
    result.append((len(set(filter(lambda x: x < y, arr)))))
for i in result:
    print(i, end=' ')