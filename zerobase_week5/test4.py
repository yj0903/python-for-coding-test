def solution(N, branches):
    answer = -1
    left, right = 0, max(branches)

    while left <= right:
        mid = (left + right) // 2
        ae = sum([i//mid for i in branches])
        if ae >= N:
            answer = mid
            left = mid + 1
        elif ae < N:
            right = mid - 1
    return answer






n = 10
b = [6, 7, 10, 16, 12]

print(solution(n, b))
