# boj11650 좌표정렬하기 실버5 - 람다표현식!
# 난이도 실버5

# 메모리 52400 KB
# 시간 4576 ms

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr = sorted(arr, key=lambda x: (x[0], x[1])) # 정렬의 우선순위 x[0] 그리고 x[1] 순서.
# 또는
arr = sorted(arr, key=lambda x: (x[0]+x[1]/1000000)) # 1000000은 입력값의 최대크기... 이런 방법도 있구만

for i, j in arr:
    print(i,j)