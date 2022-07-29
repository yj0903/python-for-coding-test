def solution(numbers, target):
    eval_set = set(numbers)
    history = set(eval_set)

    if target in eval_set:
        return 1
    
    for i in range(2, 10001):
        new_set = set()
        for x in eval_set:
            for y in numbers:
                if (x + y <= target):
                    new_set.add(x + y)
                if (x * y <= target):
                    new_set.add(x * y)

        eval_set = new_set - history
        history = history.union(eval_set)

        if target in eval_set:
            return i
        
        if len(eval_set) == 0:
            return -1

    return -1
