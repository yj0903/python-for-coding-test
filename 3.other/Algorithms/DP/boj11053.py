# boj11053 가장 긴 증가하는 부분수열 (LIS)
# 실버2

n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))



# 틀림
# n = int(input())
# arr = list(map(int, input().split()))
# pivot = arr[0]
# count = 1
#
# for i in arr:
#     if pivot < i:
#         pivot = i
#         count += 1
#         print(pivot)
# print(count)