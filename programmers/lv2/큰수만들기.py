def solution(number, k):
    answer = []
    arr = [int(i) for i in number] # 정수형 배열로 변환
    digit = len(arr) - k           # 최종 자리수
    idx = 0    # 배열 슬라이딩에 쓰일 첫 인덱스

    while digit != len(answer): # 최종자리수가 만들어질 때까지 반복
        maxValue = 0
        for i in range(idx, k+len(answer)+1):
            if maxValue < arr[i]:
                maxValue = arr[i]
                idx = i
                # 8번 10번 시간초과 방지: 9가 가장 크므로 더이상 찾을 필요 x
                if arr[i] == 9:
                    break

        # 슬라이딩 범위내에서 찾은 max 저장
        answer.append(arr[idx])
        # 슬라이딩 시작점을 한칸 이동
        idx += 1
    return ''.join([str(a) for a in answer]) # 숫자배열을 문자열로 변환하여 반환

print(solution("4177252841", 4))
