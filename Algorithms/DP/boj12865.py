# boj12865 평범한 배낭
# 골드5

# 메모리 226756 KB
# 시간 5652 ms

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for row in range(1, n + 1):
    weight, value = map(int, input().split())
    for col in range(1, k + 1):
        if col < weight:
            dp[row][col] = dp[row - 1][col]
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - weight] + value)

print(dp[n][k])


# 틀린 코드 ( dp 없이 )

# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# max_value = 0
#
# arr = list()
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# arr.sort()
# arr.sort(key=lambda x: x[1], reverse=True)
# print(arr)
# for i in range(len(arr)):
#     weight = 0
#     value = 0
#     for array in arr[i:]:
#         if k - weight >= array[0]:
#             weight += array[0]
#             value += array[1]
#     max_value = max(max_value, value)
# print(max_value)