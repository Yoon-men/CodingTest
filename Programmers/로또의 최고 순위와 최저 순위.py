# Link : https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3#fn1

def solution(lottos, win_nums) : 
    # 번호 일치 확인
    nice = 0
    for i in lottos : 
        if i in win_nums : 
            nice += 1

    # 행복회로 풀가동
    happinessCircuit = lottos.count(0)
    
    # result = [(행복회로 가동된 등수), (개같이 멸망한 등수)]
    result = []

    # 행복회로 가동된 등수
    if nice + happinessCircuit == 6 : 
        result.append(1)
    elif nice + happinessCircuit == 5 : 
        result.append(2)
    elif nice + happinessCircuit == 4 : 
        result.append(3)
    elif nice + happinessCircuit == 3 : 
        result.append(4)
    elif nice + happinessCircuit == 2 : 
        result.append(5)
    else : 
        result.append(6)
    
    # 개같이 멸망한 등수
    if nice == 6 : 
        result.append(1)
    elif nice == 5 : 
        result.append(2)
    elif nice == 4 : 
        result.append(3)
    elif nice == 3 : 
        result.append(4)
    elif nice == 2 : 
        result.append(5)
    else : 
        result.append(6)
    
    # 결과
    return result