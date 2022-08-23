# boj13305 주유소
# 실버4

# 메모리 45388 KB
# 시간 148 ms

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
bill = 0

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    bill += distance[i] * min_price

print(bill)
