# 백준10709 : 기상캐스터
import sys; input = sys.stdin.readline
from typing import List

def joyGo(H: int, W: int, sky: List[List[str]]) -> List[List[int]]: 
    ans = [[-1] * W for _ in range(H)]

    for i in range(H): 
        for j in range(W): 
            crt_sky = sky[i][:j+1]
            try: 
                ans[i][j] = crt_sky[::-1].index('c')
            except ValueError: 
                pass

    return ans



if __name__ == "__main__": 
    H, W = map(int, input().split())
    sky = [list(input()) for _ in range(H)]

    for row in joyGo(H, W, sky): 
        print(*row)



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, H, W, sky, ans"), 
    [
        (
            1, 
            3, 4, 
            [['c', '.', '.', 'c'], ['.', '.', 'c', '.'], ['.', '.', '.', '.']], 
            [[0, 1, 2, 0], [-1, -1, 0, 1], [-1, -1, -1, -1]]
        ), 
        (
            2, 
            6, 8, 
            [['.', 'c', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'c', 'c', 'c', '.', '.', 'c', '.'], ['.', '.', '.', '.', 'c', '.', '.', '.'], ['.', '.', 'c', '.', 'c', 'c', '.', '.'], ['.', '.', '.', '.', 'c', '.', '.', '.']], 
            [[-1, 0, 1, 2, 3, 4, 5, 6], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 1, 2, 0, 1], [-1, -1, -1, -1, 0, 1, 2, 3], [-1, -1, 0, 1, 0, 0, 1, 2], [-1, -1, -1, -1, 0, 1, 2, 3]]
        )
    ]
)

def test_joyGo(case_num: int, H: int, W: int, sky: List[List[str]], ans: List[List[int]]) -> None: 
    res = joyGo(H, W, sky)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ