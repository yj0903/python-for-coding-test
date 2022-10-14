# 실버2
# 시간 4544ms (심각하다..)

n = int(input())
arr = [[i for i in input()] for _ in range(n)]
answer = 0

dx = [0, 1]
dy = [1, 0]

for i in range(n):
    for j in range(n):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]

            # 두 지점이 배열 내에 있고
            if (0 <= nx < n) and (0 <= ny < n):
                # 두 지점의 색이 다를 때
                if arr[i][j] != arr[nx][ny]:

                    # (1) swap
                    arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

                    # (2) 가로 기준 가장 긴 수열 찾기
                    for row in range(n):
                        count = 1
                        for col in range(n - 1):
                            if arr[row][col] == arr[row][col + 1]:
                                count += 1
                                answer = max(answer, count)
                            else:
                                count = 1

                    # (3) 세로 기준 가장 긴 수열 찾기
                    for col in range(n):
                        count = 1
                        for row in range(n - 1):
                            if arr[row][col] == arr[row + 1][col]:
                                count += 1
                                answer = max(answer, count)
                            else:
                                count = 1

                    # (4) 원상 복구 swap
                    arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

print(answer)
