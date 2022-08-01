# boj9461 파도반 수열 (DP)

import sys

m = int(sys.stdin.readline())

for i in range(m):
    n = int(sys.stdin.readline())

    # 점화식 세우는 게 중요
    dp = [0] * 101
    dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, n+1): # len(arr)이던, n+1이던 실행 시간에 큰 영향 X
        dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[n])
