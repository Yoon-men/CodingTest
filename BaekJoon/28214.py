# 백준28214 : 크림빵
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, K: int, P: int, breads: List[int]) -> int: 
    cnt = 0

    for i in range(0, N*K - K + 1, K): 
        if sum(breads[i:i+K]) > K - P: 
            cnt += 1

    return cnt


if __name__ == "__main__": 
    N, K, P = map(int, input().split())
    breads = list(map(int, input().split()))
    print(joyGo(N, K, P, breads))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, K, P, breads, ans"), 
    [
        (
            1, 
            2, 3, 2, [1, 1, 0, 1, 0, 0], 
            1
        ), 
        (
            2, 
            3, 2, 1, [1, 1, 0, 0, 1, 1], 
            2
        )
    ]
)

def test_joyGo(case_num: int, N: int, K: int, P: int, breads: List[int], ans: int) -> None: 
    res = joyGo(N, K, P, breads)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ