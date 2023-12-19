answer = []

def recur(numbers, idx, checked, ans):
    if idx == len(numbers):
        answer.append(ans)
        return

    for i in range(len(numbers)):
        if not checked[i]:
            checked[i] = True
            recur(numbers, idx + 1, checked, ans + str(numbers[i]))
            checked[i] = False

def solution(numbers):
    # 재귀 이용한 완전 탐색
    n = len(numbers)
    checked = [False] * (n + 1)
    recur(numbers, 0, checked, '')

    # 가장 큰 값 구하기
    array = [int(a) for a in answer]
    return str(max(array))

print(solution([6, 10, 2]))