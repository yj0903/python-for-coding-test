# 체육복

def solution(n, lost, reserve):
    clothes = [1] * n  # n명 모두 체육복 1벌씩
    studentNum = n
    for l in lost:
        clothes[l - 1] -= 1  # 잃어버렸으면 -1
    for r in reserve:
        clothes[r - 1] += 1  # 여분 있으면 +1

    for i in range(n):
        if clothes[i] == 0:
            if (i != 0) and (clothes[i - 1] == 2):
                clothes[i - 1] = 1
                clothes[i] = 1
            elif (i != n - 1) and (clothes[i + 1] == 2):
                clothes[i + 1] = 1
                clothes[i] = 1
            else:
                studentNum -= 1
    return studentNum


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
