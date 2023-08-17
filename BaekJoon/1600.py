# 백준1600 : 말이 되고픈 원숭이
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(K: int, W: int, H: int, _map: List[List[int]]) -> int : 
    def BFS() -> int : 
        dx, dy = [-1,1,0,0], [0,0,1,-1]
        ddx, ddy = [-2,-1,1,2,2,1,-1,-2], [1,2,2,1,-1,-2,-2,-1]
        visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

        dq = deque([(0, 0, K)])
        while dq : 
            x, y, z = dq.popleft()

            if (x == H-1) and (y == W-1) : return visited[x][y][z]

            if z > 0 : 
                for i in range(8) : 
                    nx, ny = x+ddx[i], y+ddy[i]
                    if (0 <= nx < H) and (0 <= ny < W) and (_map[nx][ny] != 1) and (not visited[nx][ny][z-1]) : 
                        dq.append((nx, ny, z-1))
                        visited[nx][ny][z-1] = visited[x][y][z] + 1

            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < H) and (0 <= ny < W) and (_map[nx][ny] != 1) and (not visited[nx][ny][z]) : 
                    dq.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1

        return -1


    return BFS()



if __name__ == "__main__" : 
    K = int(input())
    W, H = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(H)]

    print(joyGo(K, W, H, _map))