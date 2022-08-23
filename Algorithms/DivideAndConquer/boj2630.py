# boj2630 색종이 만들기
# 메모리 30840 KB
# 시간 100 ms

n = int(input())
array = [list(map(int, input().split())) for i in range(n)]

count = [0, 0]
start = [0, 0]
end = [n, n]


def dc(start, end):
    x1, y1 = start
    x2, y2 = end

    # 탈출조건
    if (x2 - x1 < 1) or (y2 - y1 < 1):
        return

    global count
    black, white = False, False

    # 1) 리스트 슬라이싱 사용
    # for y in range(y1, y2):
    #     if 1 in array[y][x1:x2]:
    #         black = True
    #     if 0 in array[y][x1:x2]:
    #         white = True
    #     if black and white:
    #         break

    # 2) 이중 반복문 사용
    for y in range(y1, y2):
        for x in range(x1, x2):
            if 1 == array[y][x]:
                black = True
            if 0 == array[y][x]:
                white = True
            if black and white:
                break

    if black and not white:
        count[1] += 1
    elif not black and white:
        count[0] += 1
    else:
        # 재귀함수 도입부
        # 1 좌 상
        dc([x1, y1], [(x1 + x2) // 2, (y1 + y2) // 2])
        # 2 좌 하
        dc([x1, (y1 + y2) // 2], [(x1 + x2) // 2, y2])
        # 3 우 상
        dc([(x1 + x2) // 2, y1], [x2, (y1 + y2) // 2])
        # 4 우 하
        dc([(x1 + x2) // 2, (y1 + y2) // 2], [x2, y2])


dc(start, end)
print('\n'.join(map(str, count)))
