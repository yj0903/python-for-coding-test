#================================
# 재귀함수 
def recursive_function(i):
  if i == 100:
    return 
  print(i,"번째 재귀함수에서 ",i+1,"번째 재귀함수를 호출")
  recursive_function(i+1)
  print(i,"번째 재귀함수 종료")

recursive_function(1)


#================================
# 팩토리얼 예제

def factorial(n):
  if n <=1: 
    print(n)
    return 1
  print(n,end='*')
  return n*factorial(n-1)

print(factorial(10))

#================================
# 유클리드호제법 예제 GCD
# A, B (A>B)의 최대공약수 = B, R(A%B)의 최대공약수
def GCD(a, b):
  # exit
  if (a % b == 0): 
    return b
  # recursive
  return GCD(b, a%b)
  
print(GCD(192,162))
