# boj5397 키로거
# 실버2

# 메모리 41660KB
# 시간 1640ms

import sys

n = int(sys.stdin.readline())

for i in range(n):
    left_stack = list()
    right_stack = list()
    keys = sys.stdin.readline()

    for key in keys:
        if key == '<': # 왼쪽 커서 이동
            if left_stack:
                right_stack.append(left_stack.pop())
        elif key == '>': # 오른쪽 커서 이동
            if right_stack:
                left_stack.append(right_stack.pop())
        elif key == '-': # 값 지움
            if left_stack:
                left_stack.pop()
        elif '0' <= key <= '9' or 'a' <= key <= 'z' or 'A' <= key <= 'Z':
            left_stack.append(key)
    print(''.join(left_stack) + ''.join(right_stack[::-1]))
