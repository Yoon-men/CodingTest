# 백준1245 : 농장 관리
import sys ; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(x, y) : 
    global chk
    visited[x][y] = 1
    for i in range(8) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M) : 
            if graph[x][y] < graph[nx][ny] : 
                chk = 0
            if (not visited[nx][ny]) and (graph[nx][ny] == graph[x][y]) : 
                joyGo(nx, ny)
    

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    visited = [[0]*M for _ in range(N)]

    ans = 0
    for i in range(N) : 
        for j in range(M) : 
            if (graph[i][j] > 0) and (not visited[i][j]) : 
                chk = 1
                joyGo(i, j)
                if chk : ans += 1
    
    print(ans)