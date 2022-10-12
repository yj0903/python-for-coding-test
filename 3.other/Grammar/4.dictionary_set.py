# 사전 Dictionary & 집합 Set

# dict() 
# (중요) 순서 없음. 인덱싱 X
# key:value 키와 값의 쌍
# json 형태
# Hash Table 이용: O(1) 시간

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("사과가 있습니다.")


# 키만 추출: keys()
  key_list = data.keys()
  print('키: ',key_list)
# 값만 추출: valuse()
  value_list = data.values()
  print('값: ',value_list)



for key in key_list:
  print(data[key])
# for value in value_list:
#  print(data[value]) # X


#================
# 집합
# 중복 X, 순서 X
# set()

data = set([1,1,2,2,3,3,4,5])
print(data)

data = {1,1,1,2,2,2,2}
print(data)


a=set([1,2,3,4,5])
b=set([3,4,5,6,7])
# 합집합
print('합: ',a|b)
# 교집합
print('교: ',a&b)
# 차집합
print('차: ',a-b)


data=set([1,2,3])
print(data)
# .add
data.add(4)
print('add ', data)
# .update
data.update([5,6,7])
print('update ', data)
# .remove
data.remove(3)
print('remove ', data)