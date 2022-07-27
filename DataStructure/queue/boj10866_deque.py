# boj10866 덱 (실버4)

from collections import deque
import sys

n = int(input('숫자 입력'))
dq = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(dq) != 0:
            print(dq[len(dq) - 1])
        else:
            print(-1)
