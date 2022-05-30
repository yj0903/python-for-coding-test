# 조건문 반복문

# if 조건문
x = int(input())
if x>=10:
  print("x>=10")
if x>=0:
  print("x>=0")
if x > 30:
  print("x>=30")

# 들여쓰기 기준
score = int(input())
if score >= 70:
  print("성적 70점 이상")
  if score >= 90:
    print("성적이 우수합니다.")
else:
  print("성적이 70점 미만입니다.")
  print("조금 더 분발하세요")
print("---종료---")


a=int(input())
if a<5:
  print("5 미만")
elif a==10:
  print("10이다")
else:
  print("그 외")

# pass
# 조건문 형태는 만들고 처리부분 비워놓을때
score = int(input())
if score >= 80:
  pass
else:
  print("80 못 넘었음")




#===================
# 반복문 for 간결함

for i in range(10):
  print(i)

# continue
for i in range(10):
  if i%2 == 0:
    continue
  print(i)
