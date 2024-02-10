# 백준1735 : 분수 합
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(A: int, B: int, C: int, D: int) -> Tuple[int, int]: 
    def getGCD(x: int, y: int) -> int: 
        while y != 0: 
            z = x % y
            x = y
            y = z
        
        return x


    numerator, dominator = (A*D + B*C), (B * D)
    gcd = getGCD(numerator, dominator)

    return (numerator//gcd, dominator//gcd)



if __name__ == "__main__": 
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(*joyGo(A, B, C, D))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, A, B, C, D, ans"), 
    [
        (
            1, 
            2, 7, 
            3, 5, 
            (31, 35)
        )
    ]
)

def test_joyGo(case_num: int, A: int, B: int, C: int, D: int, ans: Tuple[int, int]) -> None: 
    res = joyGo(A, B, C, D)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ