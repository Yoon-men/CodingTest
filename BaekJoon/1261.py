# 백준1261 : 알고스팟
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(M: int, N: int, maze: List[List[str]]) : 
    dx, dy = [-1,1,0,0], [0,0,1,-1]

    dq = deque([(0, 0)])
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == -1) : 
                if (maze[nx][ny] == '0') : 
                    visited[nx][ny] = visited[x][y]
                    dq.appendleft((nx, ny))
                else : 
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append((nx, ny))
    
    return visited[N-1][M-1]


if __name__ == "__main__" : 
    M, N = map(int, input().split())
    maze = [list(input().strip()) for _ in range(N)]

    print(joyGo(M, N, maze))