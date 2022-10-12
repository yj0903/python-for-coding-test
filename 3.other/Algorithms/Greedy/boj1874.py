# boj 1874 스택수열
# 난이도 실버2

# 메모리 33448 KB
# 시간 496 ms


import sys

stack_list = list()
queue_list = list()
result = list()
n = int(sys.stdin.readline())

for i in range(1, n + 1):
    k = int(sys.stdin.readline())
    stack_list.append(i)
    queue_list.append(k)
    result.append('+')

    # 스택 최상위 원소와 데이터가 같을 때 뽑을 수 있음.
    while True:
        if (len(stack_list) == 0) and (len(queue_list) == 0):
            break

        if stack_list[-1] == queue_list[0]:
            stack_list.pop()
            queue_list.pop(0)
            result.append('-')
        else:
            break

if len(stack_list) != 0 and len(queue_list) != 0:
    print("NO")
else:
    for c in result:
        print(c)