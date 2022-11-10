# 백준1058 : 친구
import sys ; input = sys.stdin.readline
from collections import deque

def joyGo(p) : 
    dq = deque([(p, 0)])
    visited = [0] * N
    visited[p] = 1
    cnt = 0

    while dq : 
        person, chk = dq.popleft()
        if chk >= 2 : continue
        for i in range(N) : 
            if not visited[i] and graph[person][i] : 
                visited[i] = 1
                cnt += 1
                dq.append((i, chk+1))

    return cnt

if __name__ == "__main__" : 
    N = int(input())
    graph = [[0]*N for _ in range(N)]

    for i in range(N) : 
        Li = list(input().strip())
        for j in range(N) : 
            if Li[j] == "Y" : graph[i][j] = 1
    
    ans = 0
    for i in range(N) : 
        ans = max(ans, joyGo(i))
    print(ans)