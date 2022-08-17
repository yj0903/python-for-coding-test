n, m = map(int, input().split())
arr = list()
[arr.append(min(list(map(int, input().split())))) for _ in range(n)]

print(max(arr))