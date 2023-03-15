# 백준1113 : 수영장 만들기
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(x: int, y: int, height: int) -> int : 
    dq = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    outFlag = 0

    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) : 
                if (not visited[nx][ny]) and (graph[nx][ny] <= height) : 
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
            else : 
                outFlag = 1
    
    return cnt if not outFlag else 0


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]

    dx, dy = [-1,1,0,0], [0,0,1,-1]

    ans = 0
    for height in range(1, 9) : 
        visited = [[0]*M for _ in range(N)]
        for i in range(N) : 
            for j in range(M) : 
                if (not visited[i][j]) and (graph[i][j] <= height) : 
                    ans += joyGo(i, j, height)

    print(ans)