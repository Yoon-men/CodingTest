# 백준11003 : 최솟값 찾기
import sys; input = sys.stdin.readline
from collections import deque

def joyGo() : 
    dq = deque()
    ansLi = [0] * N

    for i in range(N) : 
        while (dq) and (dq[0][0] < i-L+1) : 
            dq.popleft()
        while (dq) and (dq[-1][1] >= Li[i]) : 
            dq.pop()

        dq.append((i, Li[i]))
        ansLi[i] = dq[0][1]
    
    return ansLi


if __name__ == "__main__" : 
    N, L = map(int, input().split())
    Li = list(map(int, input().split()))

    print(*joyGo())