# 백준1987 : 알파벳
import sys; input = sys.stdin.readline
from typing import List

def joyGo(R: int, C: int, board: List[List[str]]) -> int: 
    def DFS(s: str, x: int, y: int) -> None: 
        nonlocal ans
        ans = max(ans, len(s))
        
        for i in range(4): 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < R) and (0 <= ny < C) and (not board[nx][ny] in s): DFS(s + board[nx][ny], nx, ny)


    ans = 0
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    DFS(board[0][0], 0, 0)
    
    return ans



if __name__ == "__main__": 
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    print(joyGo(R, C, board))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, R, C, board, ans"), 
    [
        (1, 2, 4, [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']], 3), 
        (2, 3, 6, [['H', 'F', 'D', 'F', 'F', 'B'], ['A', 'J', 'H', 'G', 'D', 'H'], ['D', 'G', 'A', 'G', 'E', 'H']], 6), 
        (3, 5, 5, [['I', 'E', 'F', 'C', 'J'], ['F', 'H', 'F', 'K', 'C'], ['F', 'F', 'A', 'L', 'F'], ['H', 'F', 'G', 'C', 'F'], ['H', 'M', 'C', 'H', 'H']], 10)
    ]
)

def test_joyGo(case_num: int, R: int, C: int, board: List[List[str]], ans: int) -> None: 
    res = joyGo(R, C, board)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ
