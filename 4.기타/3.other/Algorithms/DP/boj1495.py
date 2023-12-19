# boj1495 기타리스트
# 실버1

# n, s, m = map(int, input().split())
# volumes = list(map(int, input().split()))
# result = -1


# def dp(v, arr):
#     global result
#     plus = v + arr[0]
#     minus = v - arr[0]
#
#     # 탈출조건
#     if len(arr) == 1:
#         if plus <= m:
#             result = max(result, plus)
#         if minus >= 0:
#             result = max(result, minus)
#         return
#
#     # 재귀
#     if plus <= m:
#         dp(plus, arr[1:])
#
#     if minus >= 0:
#         dp(minus, arr[1:])
#
#
# dp(s, volumes)
# print(result)


n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 0:
            continue
        if j - volumes[i-1] >= 0:
            dp[i][j-volumes[i-1]] = 1
        if j + volumes[i-1] <= m:
            dp[i][j+volumes[i-1]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)

