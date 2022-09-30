# 체육복

def solution(n, lost, reserve):
    answer = [1] * n
    count = 0

    for l in lost:
        answer[l - 1] -= 1

    for r in reserve:
        answer[r - 1] += 1

    for i in range(n):
        if answer[i] == 0:
            if i == 0:
                if answer[i+1] == 2:
                    answer[i] += 1
                    answer[i+1] -= 1
                else:
                    count += 1

            elif i == n-1:
                if answer[i-1] == 2:
                    answer[i] += 1
                    answer[i-1] -= 1
                else:
                    count += 1
            else:
                if answer[i-1] == 2:
                    answer[i] += 1
                    answer[i-1] -= 1
                elif answer[i+1] == 2:
                    answer[i] += 1
                    answer[i+1] -= 1
                else:
                    count += 1
    return n-count


print(solution(5, [1, 2, 3], [2, 3, 4]))
