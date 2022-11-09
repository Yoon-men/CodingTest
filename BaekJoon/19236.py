# 백준19236 : 청소년 상어
import sys ; input = sys.stdin.readline
from copy import deepcopy

def joyGo(x, y, amount, graph) : 
    global ans
    amount += graph[x][y][0]
    graph[x][y][0] = 0
    ans = max(ans, amount)
    
    for fish in range(1, 17) : 
        f_x, f_y = -1, -1
        for i in range(4) : 
            for j in range(4) : 
                if graph[i][j][0] == fish : 
                    f_x, f_y = i, j
                    break
        if (f_x != -1) and (f_y != -1) : 
            f_d = graph[f_x][f_y][1]        # f_d = fish_direction
            for i in range(8) : 
                nd = (f_d+i) % 8
                nx = f_x + dx[nd]
                ny = f_y + dy[nd]
                if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == x and ny == y) : continue
                graph[f_x][f_y][1] = nd
                graph[f_x][f_y], graph[nx][ny] = graph[nx][ny], graph[f_x][f_y]
                break

    d = graph[x][y][1]
    for i in range(1, 5) : 
        nx = x + dx[d]*i
        ny = y + dy[d]*i
        if (0 <= nx < 4) and (0 <= ny < 4) and (graph[nx][ny][0]) : 
            joyGo(nx, ny, amount, deepcopy(graph))

if __name__ == "__main__" : 
    graph = [[] for _ in range(4)]
    for i in range(4) : 
        Li = list(map(int, input().split()))
        m = [[] for _ in range(4)]
        for j in range(4) : 
            m[j] = [Li[2*j], Li[2*j+1] - 1]         # [번호, 방향 - 1]
        graph[i] = m

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    ans = 0
    
    joyGo(0, 0, 0, graph)
    print(ans)