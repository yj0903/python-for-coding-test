# boj1644 소수의 연속합
# 골드 3

import sys


def primes(n):  # 에라토스테네스의 체
    if n < 2:
        return [0]
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False
    return [k for k in range(2, n + 1) if is_prime[k]]


n = int(sys.stdin.readline())
prime_array = primes(n)
sum_prime_array = [0]

# 소수의 누적. 이 문법을 제대로 이해해야함.... 왜 필요한지도!
[sum_prime_array.append(sum_prime_array[i] + prime_array[i]) for i in range(len(prime_array))]

# left <= n인 동안에 슬라이싱 함.
left, right, count = 0, 1, 0
while right <= len(prime_array):

    # 여기 sum 함수를 쓰면 오랜 시간을 소요한다.. 그래서 누적한 배열 하나 만든 것.
    total = sum_prime_array[right] - sum_prime_array[left]
    if total == n:
        count += 1
        left += 1
        right = left + 1
    elif total > n:
        left += 1
        right = left + 1
    elif total < n:
        right += 1

print(count)
