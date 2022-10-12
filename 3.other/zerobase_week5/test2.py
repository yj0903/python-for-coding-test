
def solution(numbers):
    answer = ''

    strings = list(map(str, numbers))
    dic = {i: [] for i in range(1, 10)}
    for s in strings:
        # print(s[0])
        dic[int(s[0])].append(s)

    for i in range(9, 0, -1):
        if len(dic[i]) == 0:
            continue
        elif len(dic[i]) == 1:
            answer += dic[i][0]
        else:
            # 여기가 문제...
            # 3, 30, 34, 333 ... 얘네들을 어떻게 줄 세우지?
            continue


        print(answer)
    # return ''.join(str(i) for i in numbers)


num = [10000, 10000, 9999, 10, 2]
num2 = [3, 30, 34, 5, 9]
print(solution(num))
print(solution(num2))
