# 백준17086 : 아기 상어 2
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, M: int, graph: list) -> int : 
    def BFS() : 
        while q : 
            x, y = q.popleft()
            for i in range(8) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (not graph[nx][ny]) : 
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

    dx = [-1,0,1,1,1,0,-1,-1]
    dy = [1,1,1,0,-1,-1,-1,0]
    
    q = deque([(i, j) for i in range(N) for j in range(M) if graph[i][j]])
    BFS()
    
    ans = max(max(row) for row in graph) - 1
    return ans
    


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, M, graph))