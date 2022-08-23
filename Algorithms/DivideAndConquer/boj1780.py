# boj1780 종이의 개수
# 난이도 실버2

# 메모리
# 시간
import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = [0, 0, 0]
result = list()
result_set = set()

def divideConquer(x1, y1, x2, y2):
    global result
    global result_set

    if (x2 - x1 < 3) and (y2 - y1 < 3):
        for i in range(n):
            for j in range(n):
                total[arr[x1 + i][y1 + j]] += 1
        return

    elif (x2 - x1 > 4) and (y2 - y1 > 4):
        # 재귀 9등분
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                result.append(divideConquer(x1 + i, y1 + j, x1 + i + 3, y1 + j + 3))

        [result_set.add(''.join(map(str, i))) for i in arr]
        if len(result) == 9 and len(result_set) == 1:
            for i in range(3):
                total[i] += list(result_set)[i]

            result = list()
            result_set = set()
        else:
            for i in range(3):
                total[i] += result[i]

    else:
        # 3 by 3 matrix
        count = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                count[arr[x1 + i][y1 + j]] += 1

        if 9 in count:
            count[arr[x1][y1]] = 1
        return count


divideConquer(0, 0, n, n)

print(total[-1])
print(total[0])
print(total[1])