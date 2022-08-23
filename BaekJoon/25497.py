# 백준25497 : 기술 연계마스터 임스
def joyGo() : 
    ready_1 = 0
    ready_2 = 0
    answer = 0
    for i in skills : 
        if (i=="L") or (i=="S") : 
            if i=="L" : ready_1 += 1
            else : ready_2 += 1
        elif (i=="R") or (i=="K") : 
            if i=="R" : 
                if ready_1 : 
                    answer += 1
                    ready_1 -= 1
                else : 
                    return answer
            else : 
                if ready_2 : 
                    answer += 1
                    ready_2 -= 1
                else : 
                    return answer
        else : 
            answer += 1
    return answer

if __name__ == "__main__" : 
    _ = input()
    skills = input()
    print(joyGo())