# 그리디
# 
# 
# #문제1) 거스름돈
# n = 1260
# coin = [500,100,50,10]
# count = 0

# for i in coin:
#   count=count + n//i #몫
#   n = n % i #나머지
# print(count)
# 
# 
# 
# 
# #문제2) 1이 될때까지
# #방법1: 빼고 나눈다
# n,k=map(int, input().split())
# count = 0
# while True:
#   # n이 1 되면 중지
#   if n == 1: break
#   # k로 나누어지지 않으면 
#   if n%k != 0:
#     n -= 1
#   # k로 나누어지면 나눈다
#   else:
#     n /= k
#   count += 1
# print(count)
# 
# #방법2: 빼고 나눈다
# n,k=map(int, input().split())
# count = 0
# while True:
#   # n이 1 되면 중지
#   if n == 1: break
#   # k로 나누어지지 않으면 
#   if n%k != 0:
#     n -= 1
#   # k로 나누어지면 나눈다
#   else:
#     n /= k
#   count += 1
# print(count)
# 
# 
# 
# 
# # 문제3) 곱하기 혹은 더하기
# 
# data = input()
# result = int(data[0])
# for i in range(1,len(data)) :
#   num = int(data[i])
#   if (num <= 1) or (result <=1) :
#     result += num
#   else:
#     result*=num
# print(result)
# 
# 
# 
# 
# # 문제4) 모험가 길드
# n = int(input())
# data = list(map(int, input().split()))
# 
# result = 0 # 그룹 수
# count = 0 # 그룹내 모험가 수
# for i in data:
#   count += 1 # 모험가 수 1 증가
# 
#   # 모험가수 >= 공포도 이면
#   if count >= i:
#     result += 1  # 그룹수 1 증가
#     count = 0 # 모험가 수 초기화
# 
# print(result)
    



