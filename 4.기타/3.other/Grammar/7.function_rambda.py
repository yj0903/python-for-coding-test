# 함수, 람다식

# 여기서 a는 파라미터
def funcName(a):
  print("함수명 funcName")
  print(a)
  return a


# 여기서 10, 'hello'는 매개변수
funcName(10);
funcName('hello');


# global: 전역변수 참조할때 사용
a=100
def func():
  global a 
  a += 1
  print(a)
func()


# packing, unpacking
def operator(a,b):
  add_var = a+b
  sub_var = a-b
  mul_var = a*b
  divide_var = a/b
  # packing
  return add_var,sub_var,mul_var,divide_var

# unpacking
a,b,c,d = operator(7,3)
print(a,b,c,d)


#=================
# 람다식
print((lambda a,b:a+b)(3,7))

array = [('홍길동',50), ('이순신',32), ('아무개',74)]

#1 함수로 정의 후 사용
def my_key(x):
  return x[1]
print(sorted(array, key=my_key))
#2 람다함수 사용
print(sorted(array, key=lambda x:x[1]))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a,b : a+b, list1, list2)
print(list(result))