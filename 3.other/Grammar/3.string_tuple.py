# 문자열 String  & 튜플 tuple
# 큰따옴표, 작은따옴표

data = 'hello world'
print(data)

# 백슬래쉬 이용, 따옴표 사용 가능
data="Don't you \"Python\"?"
print(data)

# 문자열 덧셈
a='Hello'
b='World'
print(a+b)

# 문자열 곱셈
a='Hi'
print(a*3)

#문자열 자료형은 인덱싱 됨
data="data"
print(data[0])
#문자열 자료형은 원소할당 안 됨
data="data"
# data[0]='g' # X


#===============
# 튜플: 선언된 값은 수정 안 됨
# () 소괄호로 선언
# 인덱싱, 슬라이싱은 가능
a=(1,2,3,4,5,6)
print(a[0]) # 인덱싱 가능
print(a[0:3]) # 슬라이싱 가능
# a[2]=5 # 원소할당 X

#(중요) 서로다른 데이터 묶어서 관리할 때 쓰임 (특히 최단경로)
student1 = (10, 'Kim')
student2 = (11, 'Hong')
print(student1)
print(student2)











