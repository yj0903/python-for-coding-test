# 실버1

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

for arr in array:
    m, n, x, y = arr

# boj 코드 (잘 됨)
    # x -= 1
    # y -= 1
    # k = x
    # while k < n * m:
    #     if k % n == y:
    #         print(k + 1)
    #         break
    #     k += m
    # else:
    #     print(-1)


# 내 코드 (안됨)
    # 모듈러(%) 이용하려면 0~m-1 0~n-1 필요함
    # -1씩 해준뒤 i값 구한 다음 +1
    x %= m
    y %= n
    answer = -1
    for i in range(1, 40001):
        if i % m == x and i % n == y:
            answer = i
            break
    print(answer)
