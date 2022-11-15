# 실버3

# 2xn 사각형
#
# n=1 이면 f(1) =1
# n=2 이면 f(2) = 1 + f(1) = 2
# n=3 이면 f(3) = f(2) +f(1) = 3
# n=4 이면 f(4) = f(3) + f(2) = 5
#
# 점화식
# f(n) = f(n-1) + f(n-2)

n = int(input())

if n <= 2:
    print(n)
else:
    memo = [0 for i in range(n + 1)]
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    print(memo[n] % 10007)
