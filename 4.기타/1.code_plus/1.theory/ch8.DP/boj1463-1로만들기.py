# 실버3

# dp :
# 조건2) 크기를 쪼갤 수 있다.
# 조건1) 작은 문제들이 큰 문제의 답을 알려준다. == 어딘가에 메모해놓아야 효율적 (memorization)
#
# 점화식
# f(1) = 0
# f(2) = 1
# f(3) = 1
# f(4) = f(3)+f(1) = 2
# f(5) = f(4)+f(1) = 2+1
# f(n) =

n = int(input())
memo = [0] * (n + 1)

memo[1] = 0
for i in range(2, n + 1):
    memo[i] = memo[i - 1] + 1

    if (i % 2 == 0) and (memo[i] > memo[i // 2] + 1):
        memo[i] = memo[i // 2] + 1
    if (i % 3 == 0) and (memo[i] > memo[i // 3] + 1):
        memo[i] = memo[i // 3] + 1

print(memo[n])