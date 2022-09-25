# 백준25632 : 소수 부르기 게임
from collections import deque

def primeChk(n) : 
    for i in range(2, int(n**0.5)+1) : 
        if n%i==0 : return 0
    return 1

if __name__ == "__main__" : 
    A, B = map(int, input().split())
    AB = deque()
    C, D = map(int, input().split())
    CD = deque()

    for i in range(A, B+1) : 
        if primeChk(i) : AB.append(i)
    for i in range(C, D+1) : 
        if primeChk(i) : CD.append(i)
    
    kyoLi = deque(set(AB)&set(CD))
    turn = 0
    while AB and CD : 
        if turn%2==0 : 
            if kyoLi : 
                target = kyoLi[0]
                AB.remove(target)
                CD.remove(target)
                kyoLi.remove(target)
            else :     
                target = AB.popleft()
                if target in CD : CD.remove(target)
        else : 
            if kyoLi : 
                target = kyoLi[0]
                CD.remove(target)
                AB.remove(target)
                kyoLi.remove(target)
            else : 
                target = CD.popleft()
                if target in AB : AB.remove(target)
        turn += 1

    print("yt" if AB else "yj")