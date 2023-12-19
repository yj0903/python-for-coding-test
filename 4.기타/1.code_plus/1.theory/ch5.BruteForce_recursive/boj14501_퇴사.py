# 실버3

n = int(input())
task = [0]
profit = [0]
answer = 0

for _ in range(n):
    t, p = list(map(int, input().split(' ')))
    task.append(t)
    profit.append(p)

def solution(i, earn):
    global answer
    # 탈출조건 1: 퇴사날
    if i == n+1: # 퇴사하는 날은 상담 못함. 여태 번거 정산하기
        answer = max(answer, earn)
        return
    # 탈출조건 2: 퇴사일이 지남
    if i > n+1: # 퇴사 이후까지 일을 못하니 이건 돈 못받음
        return

    solution(i + 1, earn)
    solution(i + task[i], earn + profit[i])

solution(1, 0)
print(answer)
