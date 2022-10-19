# 실버1 (브루트포스)

k = int(input())
arr = list(input().split(' '))
checked = [True] * 10
answer = []


def possible(x, y, op):
    if op == '<':
        if x > y:
            return False
    elif op == '>':
        if x < y:
            return False
    return True


def solution(index, ans):
    if len(ans) == k + 1:  # 숫자 k개 다 고름
        answer.append(ans)
        return

    for i in range(10):
        if checked[i]:
            if index == 0 or possible(ans[index - 1], str(i), arr[index - 1]):
                checked[i] = False
                solution(index + 1, ans + str(i))
                checked[i] = True


solution(0, '')
print(answer[-1])
print(answer[0])
