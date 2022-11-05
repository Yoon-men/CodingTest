# 백준14496 : 그대, 그머가 되어
import sys ; input = sys.stdin.readline
from collections import deque

def joyGo(a, b) : 
    dq = deque([a])
    visited = [0] * (N+1)
    visited[a] = 1

    while dq : 
        chk = dq.popleft()
        if chk == b : return visited[chk]-1
        for i in graph[chk] : 
            if not visited[i] : 
                dq.append(i)
                visited[i] = visited[chk] + 1

    return -1

if __name__ == "__main__" : 
    a, b = map(int, input().split())
    N, M = map(int, input().split())


    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(joyGo(a, b))