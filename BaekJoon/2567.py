# 백준2567 : 색종이 - 2
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(papers: List[Tuple[int, int]]) -> int: 
    ans = 0

    board = [[0] * 100 for _ in range(100)]

    for start_x, start_y in papers: 
        for i in range(start_x, start_x+10): 
            for j in range(start_y, start_y+10): 
                board[i-1][j-1] = 1
    
    dx, dy = (-1,1,0,0), (0,0,1,-1)

    for x in range(100): 
        for y in range(100): 
            if not board[x][y]: continue

            adjacent = 0
            for i in range(4): 
                nx, ny = x+dx[i], y+dy[i]

                if board[nx][ny]: 
                    adjacent += 1
            
            if adjacent == 2: 
                ans += 2
            elif adjacent == 3: 
                ans += 1

    return ans


if __name__ == "__main__": 
    papers = [tuple(map(int, input().split())) for _ in range(int(input()))]
    print(joyGo(papers))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, papers, ans"), 
    [
        (
            1, 
            [(3, 7), (5, 2), (15, 7), (13, 14)], 
            96
        )
    ]
)

def test_joyGo(case_num: int, papers: List[Tuple[int, int]], ans: int) -> None: 
    res = joyGo(papers)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ