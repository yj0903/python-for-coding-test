# 실버2
# 백트래킹

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 100 * n  # 개인별 능력치 최대100


def solution(idx, ateam, bteam):
    # 팀 매칭 실패
    if len(ateam) > n / 2 or len(bteam) > n / 2:
        return

    # 팀 매칭 되어 능력치 차이 구하면 됨.
    if idx == n:
        global answer

        aval = 0
        bval = 0
        # a팀 능력치 합
        for ax in ateam:
            for ay in ateam:
                aval += arr[ax][ay]

        # b팀 능력치 합
        for bx in bteam:
            for by in bteam:
                bval += arr[bx][by]

        answer = min(answer, abs(aval - bval))
        return

    solution(idx + 1, ateam + [idx], bteam)
    solution(idx + 1, ateam, bteam + [idx])


solution(0, [], [])
print(answer)
