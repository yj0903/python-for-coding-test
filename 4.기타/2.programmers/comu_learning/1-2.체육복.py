def solution(n, lost, reserve):
    students = [1] * (n + 1) # 모두 1벌씩
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
    for idx, s in enumerate(students):
        if s == 2: # 2벌
            if students[idx - 1] == 0: # 좌 확인
                students[idx - 1] += 1
                students[idx] -= 1
            elif (idx+1 <= n) and students[idx + 1] == 0: # 우 확인
                students[idx + 1] += 1
                students[idx] -= 1
    return len([i for i in students[1:] if i != 0])


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [1, 3, 5], [2, 4, 5]))
