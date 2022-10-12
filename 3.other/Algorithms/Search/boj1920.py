# boj1920 수찾기 (이진탐색트리)
# 난이도 실버4
import sys


def binary_search(value, start, end):
    # 탈출 코드
    if start > end:
        return 0

    mid = (start+end)//2
    if arr[mid] > value:
        return binary_search(value, start, mid-1)
    elif arr[mid] < value:
        return binary_search(value, mid+1, end)
    else:
        # 찾았음
        return 1


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

m = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))

for r in request:
    print(binary_search(r, 0, n-1))
