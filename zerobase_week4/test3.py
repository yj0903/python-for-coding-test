# 18/20

def solution(words, queries):
    answer = list()

    for query in queries:
        solve = list()
        for word in words:

            # 글자수 다르면 안됨
            if len(query) != len(word):
                continue

            right = True
            for i in range(len(query)):
                if query[i] == '?':
                    break
                if query[i] != word[i]:
                    right = False
                    break

            # 단어가 해당 됨.
            if right:
                solve.append(word)
        answer.append(solve)
    return answer


w = ["hello", "hear", "hell", "good", "goose", "children", "card", "teachable"]
q = ["he??", "g???", "childre?", "goo????", "?"]

print(solution(w, q))
