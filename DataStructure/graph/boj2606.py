# boj2606 바이러스 (BFS, DFS)

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cnt = 0
visited = [False] * (n+1)
graph = [[] for i in range(n + 1)]

for i in range(1, m + 1):
    com1, com2 = list(map(int, sys.stdin.readline().split()))
    graph[com1].append(com2)
    graph[com2].append(com1)


def dfs(pos):
    global cnt
    cnt += 1
    visited[pos] = True
    for p in graph[pos]:
        if not visited[p]:
            dfs(p)


dfs(1)
print(cnt - 1)
