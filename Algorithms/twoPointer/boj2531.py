# boj2531 회전초밥
# 실버1

# 메모리 30840
# 시간 3048

import sys

n, d, k, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

result = 0

for i in range(n):
    # 슬라이딩 윈도우의 양 포인터는 k만큼 간격 유지
    left = i
    right = i+k

    # 집합set 이용해 중복된 종류 제거.
    if right <= n:
        susi = set(arr[left:right])
    else:
        # 배열을 넘어 가면 원형리스트처럼 앞쪽으로 돌아와야함.
        susi = set(arr[left:] + arr[:right % n])

    # 쿠폰 c가 포함되어 있지 않으면 1종류 추가해줌.
    result = max(result, len(susi) if c in susi else len(susi) + 1)

print(result)