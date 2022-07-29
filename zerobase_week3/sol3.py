def solution(delay, N):
    q = []
    q.append(0)

    count = 1
    for _ in range(N):
        new_q = []
        while q:
            d = q.pop(0)
            if d == 0:
                new_q.append(0)
                new_q.append(delay)
                count += 2
            else:
                new_q.append(d - 1)
        q = new_q
    
    return count
    