# 18/20

def solution(titles, lyrics, problems):
    answer = list()

    for p in problems:
        print('p ', p)
        solve = list()
        for idx in len(lyrics):
            if lyrics[idx][:len(p)] == p:
                solve.append(titles[idx])
        answer.append(solve)
    return answer


t = ["아모르파티", "아기상어", "올챙이와개구리", "산다는건"]
l = ["산다는게다그런거지누구나빈손으로와...(후략)", "아기상어뚜루루뚜루귀여운뚜루루뚜루...(후략)",
     "개울가에올챙이한마리꼬물꼬물헤엄치다...(후략)",
     "산다는건다그런거래요힘들고아픈날도많지만...(후략)"]

p = ["산다", "아기상어", "올챙이"]

print(solution(t, l, p))
