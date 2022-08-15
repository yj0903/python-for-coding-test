def solution(s, t):
    dic = {i for i in s}
    for i in dic:
        if len(s) != len(t):
            return False
        if s.count(i) != t.count(i):
            return False
    return True

sv = "abcde"
tv = "edcba"
print(solution(sv, tv))
