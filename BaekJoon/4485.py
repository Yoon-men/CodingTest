# 백준4485 : 녹색 옷 입은 애가 젤다지?
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(i, j) : 
    dq = deque()
    dq.append((i, j))
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    
    while dq : 
        x, y = dq.popleft()
        for k in range(4) : 
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) : 
                if chkLi[nx][ny] > chkLi[x][y] + m[nx][ny] : 
                    chkLi[nx][ny] = chkLi[x][y] + m[nx][ny]
                    dq.append((nx, ny))

if __name__ == "__main__" : 
    stage = 1
    while True : 
        N = int(input())
        if N==0 : break
        m = [list(map(int, input().split())) for _ in range(N)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        chkLi = [[sys.maxsize]*N for _ in range(N)]
        chkLi[0][0] = m[0][0]

        joyGo(0, 0)
        print(f"Problem {stage}: {chkLi[N-1][N-1]}")
        stage += 1