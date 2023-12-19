# 나머지 연산
# 브론즈 5

a, b, c = map(int, input().split())
print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)
