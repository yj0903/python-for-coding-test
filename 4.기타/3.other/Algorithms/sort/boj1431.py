# boj1431 시리얼번호
# 난이도 실버3
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    serial = sys.stdin.readline().strip()
    sum = 0
    for i in range(len(serial)):
        if serial[i].isdigit():
            sum += int(serial[i])
    arr.append([serial, sum])

arr.sort() # 사전순 정렬
arr.sort(key=lambda x: (len(x[0]), x[1])) # 길이, 숫자합 순서 정려
print('\n'.join(a[0] for a in arr))

