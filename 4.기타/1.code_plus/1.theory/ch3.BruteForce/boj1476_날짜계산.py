# 실버5

e, s, m = list(map(int, input().split(' ')))
E, S, M = 0, 0, 0

arr = [16, 29, 20]
year = 1

while True:
    if (E + 1 == e) and (S + 1 == s) and (M + 1 == m):
        break
    E = (E + 1) % 15
    S = (S + 1) % 28
    M = (M + 1) % 19
    year += 1
print(year)