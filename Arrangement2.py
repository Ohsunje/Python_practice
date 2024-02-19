def solution(l, r):
    answer = []
    b = 0b000000
    while(1):
        b = b + 0b000001
        b << 1
        str_b = bin(b)
        str_d = str_b[2:]
        if l < b and b < r:
            answer.append(int(str_d) * 5)
        if len(answer)==0:
            answer.append(-1)
    print(answer)
    return answer

def main():
    l = int(input())
    r = int(input())
    print(l, r)
    solution(l,r)
    return 0

main()
