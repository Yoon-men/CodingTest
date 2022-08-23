# 백준25496 : 장신구 명장 임스
def joyGo(P) : 
    answer = 0
    for i in items : 
        if P >= 200 : 
            return answer
        else : 
            P += i
            answer += 1
    return answer

if __name__ == "__main__" : 
    P, _ = map(int, input().split())
    items = sorted(list(map(int, input().split())))
    print(joyGo(P))