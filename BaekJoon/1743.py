# 백준1743 : 음식물 피하기
import sys; input = sys.stdin.readline
from collections import deque

def BFS(x, y) : 
    dq = deque([(x, y)])
    visited[x][y] = 1

    cnt = 1
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) : 
                if (graph[nx][ny]) and (not visited[nx][ny]) : 
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    return cnt


if __name__ == "__main__" : 
    N, M, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K) : 
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visited = [[0]*M for _ in range(N)]

    ansLi = []
    for i in range(N) : 
        for j in range(M) : 
            if (graph[i][j]) and (not visited[i][j]) : ansLi.append(BFS(i, j))

    print(max(ansLi))