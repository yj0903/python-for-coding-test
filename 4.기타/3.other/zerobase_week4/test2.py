# 20/20

def solution(words, queries):
    answer = []

    for query in queries:
        cnt = 0
        for word in words:
            if query[0] != '*':
                if query[:-1] == word[:len(query)-1]:
                    cnt += 1
            else:
                if query[1:] == word[-len(query)+1:]:
                    cnt += 1
        answer.append(cnt)
    return answer


w = ["hello", "hell", "good", "goose", "children", "card", "teachable"]
q = ["hell*", "goo*", "*able", "qua*"]

print(solution(w, q))
