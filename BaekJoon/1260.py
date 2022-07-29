# 백준1260 : DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline

# Depth First Search (깊이 우선 탐색)
def dfs(n) : 
    visited[n-1] = 1
    print(n, end=" ")
    for i in graph[n-1] : 
        if visited[i-1] == 0 : 
            dfs(i)

# Breadth First Search (너비 우선 탐색)
def bfs(n) : 
    dq = deque([n])
    visited[n-1] = 1
    while dq : 
        m = dq.popleft()
        print(m, end=" ")
        for i in graph[m-1] : 
            if visited[i-1] == 0 : 
                dq.append(i)
                visited[i-1] = 1

if __name__ == "__main__" : 
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        A, B = map(int, input().split())
        graph[A-1].append(B)
        graph[B-1].append(A)
    for i in range(N) : 
        graph[i-1].sort()
    visited = [0] * N
    dfs(V)
    print()
    visited = [0] * N
    bfs(V)