# 백준11724 : 연결 요소의 개수
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(n) : 
    q = deque([n])
    visited[n] = 1
    while q : 
        m = q.popleft()
        for i in graph[m] : 
            if not visited[i] : q.append(i) ; visited[i] = 1

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1) : 
        if not visited[i] : 
            if not graph[i] : cnt += 1 ; visited[i] = 1
            else : joyGo(i) ; cnt += 1
    print(cnt)