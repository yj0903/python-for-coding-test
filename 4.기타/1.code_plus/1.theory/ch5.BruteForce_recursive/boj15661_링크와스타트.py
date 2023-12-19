# 골드5 ( python3 실패 / pypy3 성공)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 100*n


def solution(idx, ateam, bteam):
    if idx == n:
        # 팀매칭 안 됨
        if len(ateam) == 0 or len(bteam) == 0:
            return

        # 팀매칭 완료. 능력치 계산
        global answer
        aVal = 0
        bVal = 0
        for ax in ateam:
            for ay in ateam:
                if ax == ay:
                    continue
                aVal += arr[ax][ay]
        for bx in bteam:
            for by in bteam:
                if bx == by:
                    continue
                bVal += arr[bx][by]
        answer = min(answer, abs(aVal - bVal))
        return

    solution(idx + 1, ateam + [idx], bteam)
    solution(idx + 1, ateam, bteam + [idx])


solution(0, [], [])
print(answer)
