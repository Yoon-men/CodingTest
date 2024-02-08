# 백준3079 : 입국심사
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, M: int, time_required: List[int]) -> int: 
    s, e = 0, max(time_required) * M

    while s <= e: 
        m = (s+e) // 2

        pass_cnt = 0
        for time in time_required: 
            pass_cnt += m // time

        if pass_cnt >= M: 
            e = m - 1
        else: 
            s = m + 1
    
    return s


if __name__ == "__main__": 
    N, M = map(int, input().split())
    time_required = [int(input()) for _ in range(N)]

    print(joyGo(N, M, time_required))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, time_required, ans"), 
    [
        (
            1, 
            2, 6, [7, 10], 
            28
        ), 
        (
            2, 
            7, 10, [3, 8, 3, 6, 9, 2, 4], 
            8
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, time_required: List[int], ans: int) -> None: 
    res = joyGo(N, M, time_required)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ