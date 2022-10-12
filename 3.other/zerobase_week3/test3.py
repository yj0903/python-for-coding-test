answer = 1
def solution(delay, N):
    global answer

    # time out
    if N < 1:
        return answer

    # 분열 가능
    answer += 2
    # print(delay, N, answer)

    # 아메바1: 곧바로 분열
    solution(delay, N - 1)

    # 아메바2: delay만큼 휴식 후 분열
    solution(delay, N - 1 - delay)

    return answer


print(solution(1, 2))  # 5
# print(solution(2, 5))  # 17
