# 백준17142 : 연구소 3
import sys; input = sys.stdin.readline
from typing import Tuple
from collections import deque
from itertools import combinations

def joyGo(N: int, M: int, map_: Tuple[Tuple[int]]) -> int : 
    def BFS(viruses: Tuple[Tuple[int, int]]) -> int : 
        dx, dy = [-1,1,0,0], [0,0,1,-1]
        visited = [[0] * N for _ in range(N)]
        for i in range(N) : 
            for j in range(N) : 
                if map_[i][j] == 1 : visited[i][j] = -1
        for x, y in viruses : visited[x][y] = 1
        
        dq = deque([virus for virus in viruses])
        res = 0
        while dq : 
            x, y = dq.popleft()
            
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) : 
                    dq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if map_[nx][ny] != 2 : res = max(visited[nx][ny]-1, res)
        
        for row in visited : 
            if 0 in row : return sys.maxsize

        return res


    for row in map_ : 
        if 0 in row : break
    else : return 0

    ans = sys.maxsize
    virus_list = [(i, j) for i in range(N) for j in range(N) if map_[i][j] == 2]
    for viruses in tuple(combinations(virus_list, M)) : 
        ans = min(BFS(viruses), ans)
    
    return -1 if ans == sys.maxsize else ans



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    map_ = tuple(tuple(map(int, input().split())) for _ in range(N))
    print(joyGo(N, M, map_))
