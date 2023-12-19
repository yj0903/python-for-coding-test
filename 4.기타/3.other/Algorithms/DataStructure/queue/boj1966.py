# boj1966 프린터큐
# 난이도 실버3

# 메모리 30,840KB
# 시간 104ms

import sys

c = int(sys.stdin.readline())

for i in range(c):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = [[k, idx] for idx, k in enumerate(arr)]

    count = 0
    while True:

        # 0번 인덱스에 있는 값이  우선순위 높다.
        if arr[0][0] == max(arr, key = lambda x:x[0])[0]:
            # 찾고자 하는 값이다. 지금까지 출력된 개수 출력한다. break
            count += 1
            if arr[0][1] == m:
                print(count)
                break
            # 찾고자 하는 값이 아니다 pop
            else:
                arr.pop(0) # 리스트이지만 큐 처럼 쓰려면 0번 인덱스 값을 pop 해야함.

        # 우선순위 높지 않다.
        else:
            # pop 후 push 한다.
            arr.append(arr.pop(0))
