# boj11726 2xn 타일링 (실버3)
# DP 문제 (재귀 가능은 함)

# 재귀로 풀었을 때, RecursionError 발생. setrecurtionslimit을 설정해줘도 안됨.
# import sys
# sys.setrecursionlimit(10**6)
#
# def solution(n):
#     if n <= 3:
#         return n
#     return solution(n - 1) + solution(n - 2)
#
#
# n = int(sys.stdin.readline())
# print(solution(n) % 10007)



# DP(점화식)로 해결
import sys
n = int(sys.stdin.readline())
if n <= 2:
    print(n)
else:
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)
