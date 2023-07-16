# 백준1926 : 그림
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(n: int, m: int, graph: list) -> str : 
    def BFS(x, y) : 
        dq = deque([(x, y)])
        graph[x][y] = 0
        cnt = 1

        while dq : 
            x, y = dq.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < n) and (0 <= ny < m) : 
                    if graph[nx][ny] : 
                        graph[nx][ny] = 0
                        dq.append((nx, ny))
                        cnt += 1
        
        return cnt


    dx, dy = [-1,1,0,0], [0,0,1,-1]

    ans_list = []
    for i in range(n) : 
        for j in range(m) : 
            if graph[i][j] : 
                ans_list.append(BFS(i, j))

    return f"{len(ans_list)}\n{max(ans_list)}" if ans_list else "0\n0"



if __name__ == "__main__" : 
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    print(joyGo(n, m, graph))