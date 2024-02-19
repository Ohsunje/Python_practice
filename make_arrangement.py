def solution(l, r):         #프로그래머스 - 배열 만들기 2
    answer = []
    for i in range(l, r+1):
        if set(str(i)) <= {'0', '5'} and i >= 5:
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    
    return answer
