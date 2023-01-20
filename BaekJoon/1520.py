# 백준1520 : 내리막 길
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(x, y) : 
    if (x, y) == (N-1, M-1) : 
        return 1

    if visited[x][y] == -1 : 
        visited[x][y] = 0

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (graph[x][y] > graph[nx][ny]) : 
                visited[x][y] += joyGo(nx, ny)
    
    return visited[x][y]


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visited = [[-1]*M for _ in range(N)]

    print(joyGo(0, 0))