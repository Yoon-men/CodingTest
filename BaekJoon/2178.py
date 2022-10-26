# 백준2178 : 미로 탐색
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(start_x, start_y) : 
    dq = deque([(start_x, start_y)])
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (graph[nx][ny] == 1) : 
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[N-1][M-1]

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    print(joyGo(0, 0))