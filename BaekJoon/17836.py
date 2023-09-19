# 백준17836 : 공주님을 구해라!
import sys; input = sys.stdin.readline
from typing import Tuple, Union
from collections import deque

def joyGo(N: int, M: int, T: int, board: Tuple[Tuple[int]]) -> Union[int, str] : 
    def BFS() : 
        dx, dy = [-1,1,0,0], [0,0,1,-1]
        dq = deque([(0, 0)])
        visited = [[0] * M for _ in range(N)]
        visited[0][0] = 1
        holy_sword = sys.maxsize

        while dq : 
            x, y = dq.popleft()
            if (x == N-1) and (y == M-1) : 
                return min(visited[x][y]-1, holy_sword)
            elif board[x][y] == 2 : 
                holy_sword = (visited[x][y]-1) + (abs(x - (N-1)) + abs(y - (M-1)))

            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (board[nx][ny] != 1) and (not visited[nx][ny]) : 
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append((nx, ny))

        return holy_sword


    result = BFS()
    return "Fail" if (result > T) else result


if __name__ == "__main__" : 
    N, M, T = map(int, input().split())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))
    print(joyGo(N, M, T, board))