# boj 2750 수정렬하기 (브론즈2)
# 브론즈2

# -----내장함수 sort(제일 빠름)-----
# 메모리 30,840 KB
# 시간 68 ms

import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    m = int(sys.stdin.readline())
    l.append(m)
l.sort()
for i in range(n):
    print(l.pop(0))


# -----버블 정렬-----
# 메모리 30,840 KB
# 시간 180 ms

# import sys
# def bubble_sort(data):
#     for i in range(len(data) - 1):
#         swap = False
#         for j in range(len(data) - i - 1):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#                 swap = True
#         if swap == False:
#             break
#     return data
#
# n = int(sys.stdin.readline())
# l = []
# for i in range(n):
#     m = int(sys.stdin.readline())
#     l.append(m)
# # 내가 만든 정렬 함수
# l = bubble_sort(l)
#
# for i in range(n):
#     print(l.pop(0))


# -----퀵 정렬-----
# 메모리 30,840 KB
# 시간 72 ms

# import sys
# def qsort(data):
#     if len(data) <= 1:
#         return data
#     pivot = data[int(len(data)/2)]
#     left = [i for i in data if i < pivot]
#     right = [i for i in data if i > pivot]
#     return qsort(left) + [pivot] + qsort(right)
#
# n = int(sys.stdin.readline())
# l = []
# for i in range(n):
#     m = int(sys.stdin.readline())
#     l.append(m)
# # 내가 만든 정렬 함수
# l = qsort(l)
#
# for i in range(n):
#     print(l.pop(0))
