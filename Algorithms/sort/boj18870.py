# boj18870 좌표압축
# 난이도 실버2

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 중복제거 후 정렬하면, 본인의 인덱스 위치가 곧 순서
arr2 = list(sorted(set(arr)))
dic = {arr2[i]:i for i in range(len(arr2))}

print(' '.join(map(str, [dic[i] for i in arr]))) # 정수형 리스트의 출력은 이렇게 하는 것...!!!!!
