# 백준1388 : 바닥 장식
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfsJoyGo(x, y) : 
    if not visited[x][y] : 
        visited[x][y] = 1
        if graph[x][y] == "-" : 
            for dy in [-1, 1] : 
                ny = y + dy
                if (0 <= ny < M) and (graph[x][ny] == "-") : 
                    dfsJoyGo(x, ny)

        elif graph[x][y] == "|" : 
            for dx in [1, -1] : 
                nx = x + dx
                if (0 <= nx < N) and (graph[nx][y] == "|") : 
                    dfsJoyGo(nx, y)


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(input().strip()) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]
    ans = 0
    for i in range(N) : 
        for j in range(M) : 
            if not visited[i][j] : 
                dfsJoyGo(i, j)
                ans += 1

    print(ans)