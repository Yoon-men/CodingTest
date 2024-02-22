# 백준1205 : 등수 구하기
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, taesoo: int, P: int, ranking: List[int]) -> int: 
    if (N == P) and (ranking[N-1] >= taesoo): 
        return -1

    for i in range(N): 
        if taesoo >= ranking[i]: 
            return i+1
    else: 
        return N+1


if __name__ == "__main__": 
    N, taesoo, P = map(int, input().split())
    ranking = list(map(int, input().split())) if N > 0 else []

    print(joyGo(N, taesoo, P, ranking))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this liens. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, taesoo, P, ranking, ans"), 
    [
        (
            1, 
            3, 90, 10, 
            [100, 90, 80], 
            2
        ), 
        (
            2, 
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 
            -1
        ), 
        (
            3, 
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 3, 0], 
            10
        ), 
        (
            4, 
            0, 0, 50, 
            [], 
            1
        ), 
        (
            5, 
            2, 90, 10, 
            [80, 70], 
            1
        ), 
        (
            6,
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 
            -1
        ), 
        (
            7, 
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 0], 
            10
        ), 
        (
            8, 
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 2], 
            -1
        ), 
        (
            9, 
            10, 1, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 1, 1], 
            -1
        ), 
        (
            10, 
            5, 3, 3, 
            [10, 10, 3, 3, 1], 
            3
        ), 
        (
            11,
            10, 3, 10, 
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 
            8
        ), 
        (
            12, 
            4, 1, 4,
            [5, 4, 3, 2], 
            -1
        ), 
        (
            13, 
            1, 0, 10, 
            [1], 
            2
        )
    ]
)

def test_joyGo(case_num: int, N: int, taesoo: int, P: int, ranking: List[int], ans: int) -> None: 
    res = joyGo(N, taesoo, P, ranking)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this liens. > ㅛㅛㅛㅛㅛㅛ