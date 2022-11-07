# 백준1240 : 노드사이의 거리
import sys ; input = sys.stdin.readline
from collections import deque

def joyGo(s, e) : 
    visited = [0] * (N+1)
    dq = deque([s])
    visited[s] = 1
    
    while dq : 
        p = dq.popleft()
        if p == e : return visited[p]-1
        for l, d in graph[p] : 
            if not visited[l] : 
                visited[l] = visited[p] + d
                dq.append(l)

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1) : 
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    for _ in range(M) : 
        a, b = map(int, input().split())
        print(joyGo(a, b))