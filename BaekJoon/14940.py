# 백준14940 : 쉬운 최단거리
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(n: int, m: int, maps: list) -> list : 
    def whereAreYou() -> tuple[int, int] : 
        for i in range(n) : 
            for j in range(m) : 
                if maps[i][j] == 2 : return (i, j)

    def BFS(x: int, y: int) -> None : 
        dq = deque([(x, y)])
        visited[x][y] = 0
        while dq : 
            x, y = dq.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and (visited[nx][ny] == -1) : 
                    if maps[nx][ny] == 1 : 
                        visited[nx][ny] = visited[x][y] + 1
                        dq.append((nx, ny))


    dx, dy = [-1,1,0,0,], [0,0,1,-1]
    visited = [[0 if not maps[i][j] else -1 for j in range(m)] for i in range(n)]

    BFS(*whereAreYou())
    
    return visited



if __name__ == "__main__" : 
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    
    ans_list = joyGo(n, m, maps)
    for row in ans_list : 
        print(*row)