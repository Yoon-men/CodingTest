# 백준2210 : 숫자판 점프
import sys; input = sys.stdin.readline
from typing import List

def joyGo(_map: List[List[int]]) -> int : 
    def DFS(x: int, y: int, num: str) -> None : 
        if len(num) == 6 : 
            ans_set.add(num)
            return
        
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < 5) and (0 <= ny < 5) : 
                DFS(nx, ny, num+_map[nx][ny])


    dx, dy = [-1,1,0,0], [0,0,1,-1]
    ans_set = set()

    for i in range(5) : 
        for j in range(5) : 
            DFS(i, j, _map[i][j])
    
    return len(ans_set)



if __name__ == "__main__" : 
    _map = [list(input().split()) for _ in range(5)]
    print(joyGo(_map))