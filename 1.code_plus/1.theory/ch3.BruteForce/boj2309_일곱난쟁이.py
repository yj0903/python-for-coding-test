# 브론즈1
# 난쟁이 7명 합이 100

def solution(arr):
    total = sum(arr)
    for i in range(8):
        for j in range(i + 1, 9):
            if total - (arr[i] + arr[j]) == 100:
                answer = [arr[k] for k in range(9) if (k != i) and (k != j)]
                answer.sort()
                return answer


array = [int(input()) for i in range(9)]
answer = solution(array)
for i in answer:
    print(i)
