# 골드 55
n = int(input())
m = int(input())
broken_btn = [False] * 10

###########################################################
# 이 부분 추가해야 완전탐색 방법으로 런타임에러 없이 통과가 된다.
if m > 0:
    broken = list(map(int, input().split(' ')))
else:
    broken = []
###########################################################

for i in broken:
    broken_btn[i] = True

answer = abs(100-n)

def possible(number):
    if number == 0:
        if broken_btn[number]:
            return 0
        else:
            return 1
    len_num = 0
    while number > 0:
        c = number % 10
        if broken_btn[c]:
            return 0
        number = number//10
        len_num += 1

    return len_num


# 완전탐색을 하려고 한다.
# 채널은 무한대까지 있지만, 수빈이가 최대 500000까지 이동할 수 있다.
# 모든 버튼이 고장났다는 가정하에, 500000번으로 이동하려고 하면
# +버튼으로 100 -> 500000 도 가능하지만
# -버튼으로 999900 -> 500000도 가능하기 때문에
# 아래와 같은 범위로 지정함.

for i in range(500000+499900):
    len_num = possible(i)
    if len_num > 0:
        btn_press = abs(n-i)
        if answer > len_num + btn_press:
            answer = len_num + btn_press
print(answer)

