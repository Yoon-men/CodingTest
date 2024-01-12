# 백준17247 : 택시 거리
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N, M, board) -> int: 
    ones = [(i, j) for i in range(N) for j in range(M) if board[i][j]]
    
    manhattan_distance = abs(ones[0][0] - ones[1][0]) + abs(ones[0][1] - ones[1][1])
    return manhattan_distance



if __name__ == "__main__": 
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, M, board))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    "case_num, N, M, board, ans", 
    [
        (
            1, 
            3, 4, 
            [(1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 1)], 
            5
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, board: List[List[int]], ans: int) -> None: 
    res = joyGo(N, M, board)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ