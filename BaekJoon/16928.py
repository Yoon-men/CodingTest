# 백준16928 : 뱀과 사다리 게임
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo() : 
    q = deque([1])
    visited[1] = 1
    while q : 
        crnt = q.popleft()
        for dice in range(1, 7) : 
            obj = crnt + dice
            if 0 < obj <= 100 and not visited[obj] : 
                if obj in L.keys() : obj = L[obj]
                elif obj in S.keys() : obj = S[obj]
                if not visited[obj] : 
                    q.append(obj)
                    visited[obj] = 1
                    cnt[obj] = cnt[crnt] + 1
    print(cnt[100])

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    L = {}
    for _ in range(N) : 
        x, y = map(int, input().split()) ; L[x] = y
    S = {}
    for _ in range(M) : 
        u, v = map(int, input().split()) ; S[u] = v
    visited = [0]*101
    cnt = [0]*101
    joyGo()