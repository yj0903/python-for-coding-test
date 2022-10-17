# 실버3
n = int(input())
array = [int(input()) for _ in range(n)]


def solution(number, count):
    if number == 0:
        return count + 1
    elif number < 0:
        return 0
    else:
        return solution(number - 1, count) + solution(number - 2, count) + solution(number - 3, count)


for i in array:
    print(solution(i, 0))
