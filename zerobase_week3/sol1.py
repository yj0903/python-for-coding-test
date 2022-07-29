def solution(N, trust):
    if len(trust) == 0:
        return -1

    for i in range(1, N+1):
         if len(list(filter(lambda x: x[0] == i, trust))) == 0:
             if len(list(filter(lambda x: x[1] == i, trust))) == N - 1:
                 return i
    return -1
    