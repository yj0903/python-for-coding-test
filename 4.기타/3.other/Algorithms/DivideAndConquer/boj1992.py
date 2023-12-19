# boj1992 쿼드 트리
# 실버1
# 메모리 30840 KB
# 시간 68 ms

import sys

n = int(input())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

def divideConquer(x1, y1, x2, y2):
    if (x2 - x1 > 3) and (y2 - y1 > 3):
        a = divideConquer(x1, y1, (x1+x2)//2, (y1+y2)//2)
        b = divideConquer(x1, (y1+y2)//2, (x1+x2)//2, y2)
        c = divideConquer((x1+x2)//2, y1, x2, (y1+y2)//2)
        d = divideConquer((x1+x2)//2, (y1+y2)//2, x2, y2)
        if (a == b == c == d) and (a == '0' or a == '1'):
            return a
        else:
            return '(' + a + b + c + d + ')'

    else:
        x2 -= 1
        y2 -= 1
        # 4군데 확인

        if arr[x1][y1] == arr[x2][y1] == arr[x1][y2] == arr[x2][y2]:
            return arr[x1][y1]
        else:
            result = '(' + arr[x1][y1] + arr[x1][y2] + arr[x2][y1] + arr[x2][y2] + ')'
            return result

print(divideConquer(0, 0, n, n))
