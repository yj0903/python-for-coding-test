def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        arr = sorted(array[i - 1: j])
        answer.append(arr[k - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
