# n, k = map(int, input().split())
# count = 0
#
# while n != 1:
#     if n % k != 0:
#         n -= 1
#     else:
#         n //= k
#     count += 1
# print(count)

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0:
        n -= (n % k)
        count += n % k
    else:
        while n % k == 0:
            n //= k
            count += 1
print(count)
