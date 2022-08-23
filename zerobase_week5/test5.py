def solution(N, M, fry, clean):
    answer = 1000000
    arr = [f+c for f, c in zip(fry, clean)]
    minus = clean[fry.index(min(fry))]

    left, right = 0, M*min(arr)

    while left <= right:
        if right-left <= 1:
            break
        mid = (left + right)//2
        chickens = sum([mid//i for i in arr])
        if chickens >= M:
            answer = min(answer, mid - minus)
            right = mid
        elif chickens < M:
            left = mid
    return answer

n = 2
m = 20
f = [2,2,1,3]
c = [2,4,3,2]
print(solution(n, m, f, c))
