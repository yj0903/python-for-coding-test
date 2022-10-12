# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
#
# result, cnt = 0, 0
#
# for i in range(m):
#     if cnt < k:
#         result += arr[0]
#         cnt += 1
#     elif cnt == k:
#         result += arr[1]
#         cnt = 0
#
# print(result)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = 0

# m을 k+1로 나눈 몫
cnt = m // (k+1)
result += (arr[0]*k + arr[1]*1) * cnt

# m을 k+1로 나눈 나머지
cnt = m % (k+1)
result += arr[0] * cnt

print(result)
