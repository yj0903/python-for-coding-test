def solution(N, trust):
    answer = -1
    cnt = 0

    arr = [[] for _ in range(N + 1)]
    for a, b in trust:
        arr[b].append(a)

    for idx, j in enumerate(arr):
        # 마을 전원 (판사 빼고)
        if len(j) == N-1:
            cnt += 1
            answer = idx

        # 판사 여러명
        if cnt != 1:
            answer = -1

    # print(arr)
    return answer


n = 4
trust = [[1,3],[2,3]]
print(solution(n, trust))
