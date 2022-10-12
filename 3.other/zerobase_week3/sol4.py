def solution(x1, y1, x2, y2):
    set_a = {(x1, y1)}
    hist_a = set_a.copy()
    set_b = {(x2, y2)}
    hist_b = set_b.copy()

    if (x1, y1) == (x2, y2):
        return 0
    
    time = 1
    while True:
        new_set_a = set()
        new_set_b = set()

        for pos_a in set_a:
            new_set_a.add((pos_a[0] + 1, pos_a[1]))
            new_set_a.add((pos_a[0], pos_a[1] + 1))
            new_set_a.add((pos_a[0] - 1, pos_a[1]))
            new_set_a.add((pos_a[0], pos_a[1] - 1))
        
        for pos_b in set_b:
            new_set_b.add((pos_b[0] + 1, pos_b[1] + 1))
            new_set_b.add((pos_b[0] - 1, pos_b[1] + 1))
            new_set_b.add((pos_b[0] + 1, pos_b[1] - 1))
            new_set_b.add((pos_b[0] - 1, pos_b[1] - 1))
        
        new_set_a = new_set_a - hist_a
        new_set_b = new_set_b - hist_b

        for pos_a in new_set_a:
            if pos_a in new_set_b:
                return time

        set_a = new_set_a
        set_b = new_set_b

        hist_a = hist_a.union(set_a)
        hist_b = hist_b.union(set_b)

        time += 1

