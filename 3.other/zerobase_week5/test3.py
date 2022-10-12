def solution(array):
    peek = -1

    left, right = 0, len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if






    if array[idx] > array[idx-1] and array[idx] > array[idx+1]:
        peek = idx
    return peek




arr = [-3, 0, 3, 4, 5, 12, 15, 14, 12, 11]
arr2 = [-5, 4, 6, 12, 16, 17]
print(solution(arr))
print(solution(arr2))
