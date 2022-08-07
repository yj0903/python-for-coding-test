# boj1920 수찾기
# 난이도 4

import sys

n = int(sys.stdin.readline())
n_list = set(map(int, sys.stdin.readline().split())) # 중복을 제거하기 위해 set 사용

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    # 여기서 시간초과 남. 다른 검색알고리즘 사용.
    if i in n_list:
        print(1)
    else:
        print(0)
