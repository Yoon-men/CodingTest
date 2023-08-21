# 백준1987 : 알파벳
import sys; input = sys.stdin.readline
from typing import List

def joyGo(R: int, C: int, board: List[List[str]]) -> int : 
    def DFS(x: int, y: int, cnt: int) -> None : 
        global ans
        ans = max(ans, cnt)

        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < R) and (0 <= ny < C) and (not board[nx][ny] in abc_set) : 
                abc_set.add(board[nx][ny])
                DFS(nx, ny, cnt+1)
                abc_set.remove(board[nx][ny])


    dx, dy = [-1,1,0,0], [0,0,1,-1]
    abc_set = {board[0][0]}

    global ans
    ans = 0
    DFS(0, 0, 1)

    return ans



if __name__ == "__main__" : 
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    print(joyGo(R, C, board))