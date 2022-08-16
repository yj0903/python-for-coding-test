# boj1484 다이어트
# 골드5

# 1) 온라인 알고리즘 방식, 값을 따로 저장 안해놓고 그때 그때 계산해서 사용 (성능이 좋음)
# 메모리 30840 KB
# 시간 136 ms

# g = int(input().strip())
# weight = list()
#
# left, right = 1, 2
# while left < g:
#     diff = (right + left)*(right - left)
#     if diff == g:
#         weight.append(right)
#         left += 1
#     elif diff > g:
#         left += 1
#     elif diff < g:
#         if right < g:
#             right += 1
#         else:
#             left += 1
# if weight:
#     print('\n'.join(map(str, weight)))
# else:
#     print(-1)



# 2) 최대길이의 배열을 미리 만들어놓고 시작.
# 메모리 36808 KB
# 시간 180 ms
import math

g = int(input().strip())

arr = [i*i for i in range(1, 100001)]
weight = list()

left, right = 0, 1
while left < len(arr):
    diff = arr[right] - arr[left]
    if diff == g:
        weight.append(int(math.sqrt(arr[right])))
        left += 1
    elif diff > g:
        left += 1
    elif diff < g:
        if right != len(arr)-1:
            right += 1
        else:
            left += 1
if weight:
    [print(i) for i in weight]
else:
    print(-1)