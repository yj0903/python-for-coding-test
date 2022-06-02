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
    



# =========================
# 구현, 시뮬레이션, 완전탐색 유형
# 많은 연습이 필요한 분야. 
# 순열 조합 라이브러리 사용
# 2차원공간인 행렬, 방향벡터 등장 등

# #문제1) 상하좌우 문제
# n = int(input())
# plans = list(input().split())
# x, y = 1, 1

# # L R U D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# route = dict()
# route['L'] = 0
# route['R'] = 1
# route['U'] = 2
# route['D'] = 3

# for plan in plans:
#   num = route[plan]
#   nx = x + dx[num]
#   ny = y + dy[num]

#   # 공간을 벗어나면 무시, 움직이지 않음.
#   if nx < 1 or ny <1 or nx >n or ny >n: continue
#   x, y = nx, ny
  
# print(x, y)




# 문제2) 시각 문제
# 00:00:00 ~ N:59:59
# 3이 1개라도 포함되어 있는 경우의 수 구하기.
# 완전탐색(24 * 60 * 60 = 86,400초)

# hour = int(input())
# count = 0

# for i in range(hour+1):
#   for j in range(60):
#     for k in range(60):
#       # 시, 분, 초 안에 '3'이라는 문자가 있으면 카운트함.
#       if '3' in str(i)+str(j)+str(k):
#         count += 1
# print(count)





# 문제3) 왕실의 나이트
# 2칸이동 후 1칸 이동 'L자'
# 행: 1~8, 열:a~h

# # 현재위치
# input_data = input()
# row = int(input_data[1])
# # ord: 아스키코드
# column = int(ord(input_data[0])) - int(ord('a'))+1

# # print(input_data[0]) #c
# # print(int(ord(input_data[0]))) #99
# # print(int(ord('a'))) #97
# # print(int(ord(input_data[0])) - int(ord('a'))+1) #즉 c는 3

# # 방향벡터 정의
# steps = [(-2,-1),(-1,-2),
#          (1,-2),(2,-1),
#          (2,1),(1,2),
#          (-1,2),(-2,1),]
# result = 0
# for step in steps:
#   next_row = row + step[0]
#   next_column = column + step[1]
#   # 벗어나지 않으면 카운트
#   if next_row >= 1 and   next_column>=1 and next_row <= 8 and next_column<=8 : result += 1

# print(result)




#문제4) 문자열 재정렬
data = input()
result = []
value = 0

for x in data:
  # 알파벳, 숫자를 따로 저장
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)
  # 정렬
  result.sort()
  if value != 0:
    result.append(str(value))
# 리스트를 문자열로 변환하여 출력
print(''.join(result))

