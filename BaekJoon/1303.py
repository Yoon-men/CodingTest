# 백준1303 : 전쟁 - 전투
import sys ; input = sys.stdin.readline
from collections import deque

def joyGo(x, y, team) : 
    dq = deque([(x, y)])
    visited[x][y] = 1

    cnt = 1
    while dq : 
        x, y = dq.popleft()

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M) and (0 <= ny < N) and (not visited[nx][ny]) and (graph[nx][ny] == team) : 
                visited[nx][ny] = 1
                dq.append((nx, ny))
                cnt += 1

    return cnt

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(input().strip()) for _ in range(M)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    w, b = 0, 0
    visited = [[0]*N for _ in range(M)]
    for i in range(M) : 
        for j in range(N) : 
            if not visited[i][j] : 
                if graph[i][j] == "W" : w += joyGo(i, j, "W") ** 2
                else : b += joyGo(i, j, "B") ** 2

    print(w, b)