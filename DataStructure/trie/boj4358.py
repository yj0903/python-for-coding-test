# boj4358 생태학
# 실버2

import sys
arr = dict()
count = 0
while True:
    word = sys.stdin.readline().rstrip()
    if not word:
        break
    count += 1
    if word in arr:
        arr[word] += 1
    else:
        arr[word] = 1


for k in sorted(arr.keys()):
    print('{0} {1:0.4f}'.format(k, arr[k]/count * 100))
