# 실버1 (브루트포스)

k = int(input())
arr = list(input().split(' '))
checked = [True] * 10
answer = []

def isPossible(ans):
    for i in range(k):
        if arr[i] == '<':
            if ans[i] > ans[i+1]:
                return False
        if arr[i] == '>':
            if ans[i] < ans[i+1]:
                return False
    return True

def solution(check, ans):
    if len(ans) == k+1:  # 숫자 k개 다 고름
        # 여기서 부등호 검사하기
        if isPossible(ans):
            answer.append((''.join([str(i) for i in ans])))
        return

    for i in range(10):
        if check[i]:
            check[i] = False
            solution(check, ans + [i])
            check[i] = True


solution(checked, [])
print(answer[-1])
print(answer[0])