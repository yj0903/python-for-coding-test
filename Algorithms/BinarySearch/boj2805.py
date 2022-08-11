# # boj2805 나무 자르기
# # 난이도 실버2
#
# # 메모리 148396 KB
# # 시간 3284 ms
#
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# start, end = 0, max(arr)
# answer = 0
#
# # 이진 탐색 구현
# while start <= end:
#     mid = (start + end) // 2
#     tree = sum([i - mid for i in arr if i > mid])
#
#     if tree >= m:
#         answer = mid
#         start = mid + 1
#     elif tree < m: # m보다 작으면 answer 될 수 없음.
#         end = mid - 1
#
# print(answer)


# 메모리 148396 KB
# 시간 2512 ms

import sys

answer = 0

def binarySearch(left, right, array):
    global answer
    # 탈출 조건
    if left > right:
        return answer

    mid = (left + right) // 2
    tree = sum([i - mid for i in array if i > mid])

    if tree > m:
        answer = mid
        return binarySearch(mid + 1, right, array)
    elif tree == m:
        answer = mid
        return answer
    elif tree < m:
        return binarySearch(left, mid - 1, array)


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(arr)

print(binarySearch(start, end, arr))

