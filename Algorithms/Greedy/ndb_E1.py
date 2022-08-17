

n = 1260
coin = [500, 100, 50, 10]
count = 0

for i in coin:
    if n >= i:
        count += n // i
        print(i, n // i)
        n = n % i
print(count)