# boj15649 N과 M
# 실버3

# 메모리 30840 KB
# 시간 212 ms

n, m = map(int, input().split())
arr = list()

def dfs():
    # 탈출 조건 : 수열 길이가 m 됐을 때.
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    # arr에 오름차순으로 append
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop() # backtracking
dfs()


