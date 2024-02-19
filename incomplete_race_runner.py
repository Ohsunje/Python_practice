def solution(participant, completion):  #프로그래머스 - 완주하지 못한 선수
    answer = str(set(participant) - set(completion))
    countnum = {}

    if answer == "set()":
        for name in participant:
            if name in countnum:
                countnum[name] += 1
            else:
                countnum[name] = 1
        for name in completion:
            if name in countnum:
                countnum[name] -= 1
        for name, count in countnum.items():
            if count > 0:
                return name
       
    else:    
        answer2 = answer[2:len(answer)-2]
        return answer2
