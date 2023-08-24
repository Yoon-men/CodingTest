# 백준14442 : 벽 부수고 이동하기 2
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, M: int, K: int, _map: List[List[int]]) -> int : 
    def BFS() : 
        dx, dy = [-1,1,0,0], [0,0,1,-1]
        visited: List[List[List[int]]] = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
        
        dq = deque([(0, 0, K)])
        while dq : 
            x, y, z = dq.popleft()

            if (x == N-1) and (y == M-1) : return visited[x][y][z] + 1

            if z > 0 : 
                for i in range(4) : 
                    nx, ny = x+dx[i], y+dy[i]
                    if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny][z-1]) : 
                        dq.append((nx, ny, z-1))
                        visited[nx][ny][z-1] = visited[x][y][z] + 1
            
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (_map[nx][ny] != 1) and (not visited[nx][ny][z]) : 
                    dq.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
        
        return -1


    return BFS()


if __name__ == "__main__" : 
    N, M, K = map(int, input().split())
    _map = [list(map(int, input().strip())) for _ in range(N)]

    print(joyGo(N, M, K, _map))