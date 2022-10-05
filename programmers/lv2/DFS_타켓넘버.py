count = 0


def solution(numbers, target):
    dfs(0, numbers, target)
    return count


def dfs(sum, numbers, target):
    global count
    # 탈출조건
    if len(numbers) == 0:
        if sum == target:
            count += 1
            print(sum)
        return

    # 재귀
    dfs(sum + numbers[0], numbers[1:], target)
    dfs(sum - numbers[0], numbers[1:], target)


# print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))



# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers] # 모든 인자를 튜플로 만들어 리스트화 함.
#     print(l)
#     s = list(map(sum, product(*l)))
#     print(s)
#     return s.count(target)
# print(solution([4, 1, 2, 1], 4))