# 백준1351 : 무한 수열
from collections import defaultdict

def joyGo(N: int, P: int, Q: int) -> int : 
    def DFS(n: int) -> int : 
        if Di[n] : return Di[n]

        Di[n] = DFS(n//P) + DFS(n//Q)
        return Di[n]


    Di = defaultdict(int)
    Di[0] = 1

    return DFS(N)



if __name__ == "__main__" : 
    N, P, Q = map(int, input().split())
    print(joyGo(N, P, Q))