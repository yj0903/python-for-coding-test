# 골드4

# 19개(회전, 대칭 포함) 블럭 자리를 배열에 선언
blocks = (
    ((0, 1), (0, 2), (0, 3)),
    ((1, 0), (2, 0), (3, 0)),
    ((1, 0), (1, 1), (1, 2)),
    ((0, 1), (1, 0), (2, 0)),
    ((0, 1), (0, 2), (1, 2)),
    ((1, 0), (2, 0), (2, -1)),
    ((0, 1), (0, 2), (-1, 2)),
    ((1, 0), (2, 0), (2, 1)),
    ((0, 1), (0, 2), (1, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 1), (1, 0), (1, 1)),
    ((0, 1), (-1, 1), (-1, 2)),
    ((1, 0), (1, 1), (2, 1)),
    ((0, 1), (1, 1), (1, 2)),
    ((1, 0), (1, -1), (2, -1)),
    ((0, 1), (0, 2), (-1, 1)),
    ((0, 1), (0, 2), (1, 1)),
    ((1, 0), (2, 0), (1, 1)),
    ((1, 0), (2, 0), (1, -1)),
)

row, col = map(int, input().split())
arr = [list(map(int, input().split(' '))) for _ in range(row)]
answer = 0

for i in range(row):
    for j in range(col):
        for block in blocks:
            total = arr[i][j]

            for dx, dy in block:
                nx = j + dx
                ny = i + dy

                if 0 <= nx < col and 0 <= ny < row:
                    total += arr[ny][nx]
                else:
                    break
            if answer < total:
                answer = total
print(answer)
