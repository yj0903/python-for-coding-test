# 실버3

n = int(input())

if n == 1:
    print(1)
else:
    memo = [0 for i in range(n + 1)]
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    print(memo[n] % 10007)
