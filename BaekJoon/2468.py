# 백준2468 : 안전 영역
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

def DFS(x, y, h) : 
    visited[x][y] = 1
    for i in range(4) : 
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < N) and (0 <= ny < N) : 
            if (graph[nx][ny] > h) and (not visited[nx][ny]) : 
                DFS(nx, ny, h)

def BFS(x, y, h) : 
    dq = deque([(x, y)])
    visited[x][y] = 1
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N) : 
                if (graph[nx][ny] > h) and (not visited[nx][ny]) : 
                    visited[nx][ny] = 1
                    dq.append((nx, ny))


if __name__ == "__main__" : 
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    maxHeight = 0
    for i in range(N) : 
        for j in range(N) : 
            if graph[i][j] > maxHeight : maxHeight = graph[i][j]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    mode = "BFS"
    ansLi = [0] * maxHeight
    for height in range(maxHeight) : 
        visited = [[0]*N for _ in range(N)]
        cnt = 0
        for i in range(N) : 
            for j in range(N) : 
                if (graph[i][j] > height) and (not visited[i][j]) : 
                    if   mode == "DFS" : 
                        DFS(i, j, height)
                        cnt += 1
                    elif mode == "BFS" : 
                        BFS(i, j, height)
                        cnt += 1
        ansLi[height] = cnt

    print(max(ansLi))