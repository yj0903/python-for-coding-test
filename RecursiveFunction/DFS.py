# 깊이우선탐색 함수
def DFS(graph, start, visited):
  visited[start] = True
  print(start, end=' ')
  for i in graph[start]:
    if not visited[i] :
      DFS(graph, i, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph =[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9

DFS(graph, 1, visited)  