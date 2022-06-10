# 기본 입출력
# 파일 입력 또는 콘솔 입력


# input() 함수
n = int(input())
print(n)

# map() 함수
# 리스트 원소 각각에 특정 함수 적용
data = list(map(int, input().split())) # 각 원소에 int 함수 적용
print(data)


#(중요) 빠르게 입력 받기 sys
# sys.stdin.readline()
# rstrip() : 줄바꿈 기호 삭제
import sys
data = sys.stdin.readline().rstrip()
print(data)


# =================
# 출력
a=1
b=2
print(a,b)
print(7,end=' ')
print(8,end=' ')
print(9)

# f-string
# 중괄호 안에 변수명 기입 가능
answer = 7
print(f"정답은 {answer}입니다.")



