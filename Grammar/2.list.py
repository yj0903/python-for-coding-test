# 리스트 List
# 인덱스는 0부터 시작
# list 또는 []

a=[0,1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])

# 인덱싱
print(a[0])
print(a[-1])

# 슬라이싱
print(a[0:3]) # O
print(a[-1:3]) # X

# (중요) 리스트 컴프리헨션: 리스트 초기화
array = [i for i in range(10)]
print(array)

# (중요) 리스트 선언시 반복문+조건문
array = [i for i in range(20) if i%2 == 1]
print(array)
array = [i for i in range(20) if i%2 == 0]
print(array)

# (중요) 언더바 사용. 단순 반복시
for _ in range(5):
  print("Cheer Up!")

# (중요) 리스트 메서드
# .append
# .sort()
# .reverse()
# .insert(n,a)
# .count()
# .remove()

# 특정값 갖는 원소 모두 제거
a=[1,2,3,4,5,5,5,3,3,3]
remove_set = {2,3}
result = [i for i in a if i not in remove_set ]
print(result)