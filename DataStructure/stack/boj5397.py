# boj5397 키로거
# 실버2

import sys

n = int(sys.stdin.readline())

for i in range(n):
    result = list()
    cursor = 0

    keys = sys.stdin.readline()

    for key in keys:
        if key == '<':
            cursor = max(0, cursor - 1)
        elif key == '>':
            cursor = min(len(result), cursor + 1)
        elif key == '-':
            if len(result) != 0:
                result.pop()
        elif '0' <= key <= '9' or 'a' <= key <= 'z' or 'A' <= key <= 'Z':
            result.insert(cursor, key)
            cursor += 1

    print(''.join(result))