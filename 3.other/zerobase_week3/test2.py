import sys

sys.setrecursionlimit(10000)

min = 100000
flag = False


def func(cnt, numbers, target):
    global min
    global flag

    # 종료 조건1 : 계산 불가
    if target < 0:
        if not flag:
            min = -1
        return

    # 종료 조건2 : 계산 완료
    if target == 0:
        flag = True
        if min > cnt:
            min = cnt
        return min

    # 계산 중
    cnt += 1
    for n in numbers:
        # 나눗셈
        if n == 0:
            continue
        if n != 1 and target % n == 0:
            func(cnt, numbers, int(target / n))
        # 뺄셈
        else:
            func(cnt, numbers, target - n)
    return min


def solution(numbers, target):
    return func(0, numbers, target)


# print(solution([1, 4, 2], 12))  # 3
print(solution([0, 2, 4], 17))  # -1
