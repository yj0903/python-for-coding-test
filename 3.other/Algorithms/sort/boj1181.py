# boj1181 단어정렬
# 난이도 실버5

# 메모리 36112 KB
# 시간 108 ms

import sys
n = int(sys.stdin.readline())
words = set()

for i in range(n):
    word = sys.stdin.readline()
    words.add(word)

words = list(words)
words.sort(key=lambda x: (len(x), x))
print(''.join(words))

