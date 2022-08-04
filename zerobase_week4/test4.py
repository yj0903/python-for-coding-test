# 12/20

import heapq

def solution(start, time):
    answer = []
    now = 0
    que = []
    need = []

    # 우선순위 큐에 모든 데이터 넣기
    for i in range(len(start)):
        heapq.heappush(que, [start[i], time[i], i])

    # 첫번째 작업
    s, t, i = heapq.heappop(que)
    heapq.heappush(need, [t, i])

    while True:
        # 작업 종료
        if len(need) == 0 and len(que) == 0:
            break

        while need:
            if (len(need) >= 2) and (need[0][0] == need[1][0]) and (need[0][1] > need[1][1]):
                t1, i1 = heapq.heappop(need)
                t, i = heapq.heappop(need)
                heapq.heappush(need, [t1, i1])
            else:
                t, i = heapq.heappop(need)
            now += t
            answer.append(i)


            # 수시로 큐 확인해주기
            while (len(que) != 0) and now >= que[0][0]:
                s, t, i = heapq.heappop(que)
                heapq.heappush(need, [t, i])

        now += 1
    return answer



s = [0, 2, 3, 5, 6]
t = [2, 4, 2, 1, 3]

s1 = [4, 2, 7, 2, 6]
t1 = [5, 2, 5, 4, 3]
print(solution(s, t))
