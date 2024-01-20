# 백준1547 : 공
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(M: int, change_list: List[Tuple[int, int]]) -> int: 
    on_table = [1, 2, 3]

    for a, b in change_list: 
        a -= 1
        b -= 1
        on_table[a], on_table[b] = on_table[b], on_table[a]

    return on_table.index(1) + 1


if __name__ == "__main__": 
    M = int(input())
    change_list = [tuple(map(int, input().split())) for _ in range(M)]

    print(joyGo(M, change_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, M, change_list, ans"), 
    [
        (
            1, 
            4, 
            [(3, 1), (2, 3), (3, 1), (3, 2)], 
            3
        ), 
        (
            2, 
            2, 
            [(1, 2), (3, 1)], 
            2
        ), 
        (
            3, 
            5, 
            [(2, 3), (1, 3), (2, 3), (2, 1), (3, 1)], 
            3
        ), 
        (
            4, 
            9, 
            [(1, 2), (3, 2), (1, 2), (2, 1), (2, 1), (3, 2), (1, 3), (3, 1), (1, 2)], 
            1
        )
    ]
)

def test_joyGo(case_num: int, M: int, change_list: List[Tuple[int, int]], ans: int) -> None: 
    res = joyGo(M, change_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ