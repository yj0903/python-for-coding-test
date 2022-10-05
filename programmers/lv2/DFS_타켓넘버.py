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



