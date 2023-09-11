# 백준5427 : 불
import sys; input = sys.stdin.readline
from typing import Tuple, Union
from collections import deque

def joyGo(w: int, h: int, _map: Tuple[Tuple[str]]) -> Union[int, str] : 
    visited = [[0] * w for _ in range(h)]
    dq = deque()
    for i in range(h) : 
        for j in range(w) : 
            if _map[i][j] == '@' : 
                visited[i][j] = 1
                dq.appendleft((i, j))
            elif _map[i][j] == '*' : 
                visited[i][j] = -1
                dq.append((i, j))
            elif _map[i][j] == '#' : 
                visited[i][j] = -2
    dx, dy = [-1,1,0,0], [0,0,1,-1]


    while dq : 
        x, y = dq.popleft()

        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < h) and (0 <= ny < w) : 
                # 불
                if (visited[x][y] == -1) and (visited[nx][ny] >= 0) : 
                    visited[nx][ny] = -1
                    dq.append((nx, ny))
                # 상근
                elif (visited[x][y] > 0) and (visited[nx][ny] == 0) : 
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append((nx, ny))
            else : 
                if visited[x][y] == -1 : continue
                return visited[x][y]
    
    return "IMPOSSIBLE"



if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        w, h = map(int, input().split())
        _map = tuple(tuple(input().strip()) for _ in range(h))
        print(joyGo(w, h, _map))