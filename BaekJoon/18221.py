# 백준18221 : 교수님 저는 취업할래요
import sys; input = sys.stdin.readline
from typing import List
from math import sqrt

def joyGo(N: int, board: List[List[int]]) -> int: 
    '''
    성규가 자신을 랩실로 납치하려는 교수님으로부터
    도망칠 수 있으면 1, 그렇지 못하면 0을 반환한다.

    Parameters: 
        N (int): 성규와 교수님 간의 짜릿한 술래잡기가 이루어지는 N × N 크기의 공간에서의 N
        board (List[List[int]]): 짜릿한 술래잡기가 이루어지는 공간
    
    Returns: 
        int: 도망칠 수 있으면 1, 그렇지 못하면 0
    '''

    OTHER_STUDENT = 1
    SUNGKYU = 2
    PROFESSOR = 5

    sungkyu, professor = (0, 0), (0, 0)
    for i in range(N): 
        for j in range(N): 
            if board[i][j] == SUNGKYU: 
                sungkyu = (i, j)
            elif board[i][j] == PROFESSOR: 
                professor = (i, j)

    if sqrt((sungkyu[0] - professor[0])**2 + (sungkyu[1] - professor[1])**2) >= 5: 
        x1, y1 = min(sungkyu[0], professor[0]), min(sungkyu[1], professor[1])
        x2, y2 = max(sungkyu[0], professor[0]), max(sungkyu[1], professor[1])
        
        cnt = 0
        for i in range(x1, x2+1): 
            for j in range(y1, y2+1): 
                if board[i][j] == OTHER_STUDENT: 
                    cnt += 1
        
        if cnt >= 3: 
            return 1
    
    return 0

    ### ----- joyGo() ----- ###


if __name__ == "__main__": 
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, board))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, board, ans"), 
    [
        (
            1, 
            7, 
            [[0, 5, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 
            1
        ), 
        (
            2, 
            9, 
            [[0, 5, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 
            0
        ), 
        (
            3, 
            10, 
            [[0, 5, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
            1
        )
    ]
)

def test_joyGo(case_num: int, N: int, board: List[List[int]], ans: int) -> None: 
    res = joyGo(N, board)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ