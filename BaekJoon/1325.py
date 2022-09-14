# 백준1325 : 효율적인 해킹
from collections import deque
import sys ; input = sys.stdin.readline

def bfs(n) : 
    dq = deque([n])
    visited = [0]*(N+1)
    visited[n] = 1
    cnt = 1
    while dq : 
        m = dq.popleft()
        for e in graph[m] : 
            if not visited[e] : 
                visited[e] = 1
                dq.append(e)
                cnt += 1
    return cnt

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        A, B = map(int, input().split())
        graph[B].append(A)

    mx = 1
    answer = []
    for i in range(1, N+1) : 
        crnt = bfs(i)
        if crnt > mx : 
            mx = crnt
            answer.clear()
            answer.append(i)
        elif crnt==mx : 
            answer.append(i)
    print(*answer)