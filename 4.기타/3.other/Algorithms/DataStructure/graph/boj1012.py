# boj1012 유기농 배추
import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in direction:
        nx, ny = dx + x, dy + y
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if arr[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = list(map(int, sys.stdin.readline().split()))
    arr = [[0] * M for _ in range(N)]  # 가로*세로 M*N
    visited = [[False] * M for _ in range(N)]  # 가로*세로 M*N
    for _ in range(K):
        y, x = list(map(int, sys.stdin.readline().split()))
        arr[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)
