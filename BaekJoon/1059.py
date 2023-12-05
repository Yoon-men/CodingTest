# 백준1059 : 좋은 구간
import sys; input = sys.stdin.readline
from typing import List

def joyGo(L: int, S: List[int], n: int) -> int: 
    if n in S: return 0

    S.sort()

    s, e = 0, 0
    for num in S: 
        if n > num: s = num
        else: 
            e = num

            s, e = s+1, e-1
            return (n-s) * (e -n+1) + (e - n)


if __name__ == "__main__": 
    L = int(input())
    S = list(map(int, input().split()))
    n = int(input())

    print(joyGo(L, S, n))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, L, S, n, ans"), 
    [
        (1, 4, [1, 7, 14, 10], 2, 4), 
        (2, 5, list(map(int, "4 8 13 24 30".split())), 10, 5), 
        (3, 5, list(map(int, "10 20 30 40 50".split())), 30, 0), 
        (4, 8, list(map(int, "3 7 12 18 25 100 33 1000".split())), 59, 1065)
    ]
)

def test_joyGo(case_num: int, L: int, S: List[int], n: int, ans: int) -> None: 
    res = joyGo(L, S, n)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ