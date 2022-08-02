# boj11399 ATM (Greedy)
# 난이도 실버4

# 내 풀이 (68ms)
import sys
n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

# 현재 시점에서 가장 최선인 것 = 오름차순으로 정렬
line.sort()

waiting_time = 0
result = list()
sum = 0

for l in line:
    waiting_time = waiting_time + l
    result.append(waiting_time)

for i in result:
    sum += i
print(sum)


# 두번째 풀이 (132ms)

# import sys
# N = int(sys.stdin.readline())
# seconds = list(map(int, sys.stdin.readline().split()))
#
# # 현재 시점에서 가장 최선인 것 = 오름차순으로 정렬
# seconds.sort()
#
# minimum = 0
#
# for i in range(N):
#     for j in range(i + 1):
#         minimum += seconds[j]
# print(minimum)