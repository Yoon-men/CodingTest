# 백준1189 : 컴백홈
import sys ; input = sys.stdin.readline

def joyGo(x, y, cnt) : 
    visited[x][y] = 1
    if (x, y) == (0, C-1) :         # 목적지에 도착했다면?
        if cnt == K : global ans ; ans += 1
        return
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and (not visited[nx][ny]) and (m[nx][ny] != "T") : 
            visited[nx][ny] = 1
            joyGo(nx, ny, cnt+1)
            visited[nx][ny] = 0     # 다른 방법도 찾아야 하니까 0으로 돌려놓음

if __name__ == "__main__" : 
    R, C, K = map(int, input().split())
    m = [list(input().strip()) for _ in range(R)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    ans = 0
    visited = [[0]*C for _ in range(R)]
    joyGo(R-1, 0, 1)

    print(ans)