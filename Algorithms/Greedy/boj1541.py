# boj1541 잃어버린 괄호
# 실버2

# 메모리 30840 KB
# 시간 	68 ms

equals = input()
equals = equals.split('-')
equals = [equal.split('+') for equal in equals]

min_val = sum([int(x) for x in equals[0]])

for equal in equals[1:]:
    min_val -= sum([int(x) for x in equal])

print(min_val)