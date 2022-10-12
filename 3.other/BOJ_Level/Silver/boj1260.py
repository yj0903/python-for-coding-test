# DFS와 BFS
from collections import deque

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

# 큐 구조 사용
def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 그래프 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 간선 정렬
for g in graph:
    g.sort()


# dfs 함수 호출
visited = [False] * (n + 1)
dfs(v, graph, visited)

print()

# # bfs 함수 호출
visited = [False] * (n + 1)
bfs(v, graph, visited)