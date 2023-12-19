# 실버4

# 백준 풀이 (잘 됨, 60ms)
n = int(input())
answer = 0
start = 1
length = 1
while start <= n:
    end = start*10-1
    if end > n:
        end = n

    answer += (end-start+1)*length
    start *= 10
    length += 1

print(answer)

# 내 풀이 (잘 됨, 68ms)

# n = int(input())
# arr = [i * (10**i - 10**(i - 1)) for i in range(9)]
#
# num_len = len(str(n))
# result = sum(arr[:num_len]) + (n - 10**(num_len - 1) + 1) * num_len
# print(int(result))




