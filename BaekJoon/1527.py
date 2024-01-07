# 백준1527 : 금민수의 개수
import sys; input = sys.stdin.readline
from itertools import product

def joyGo(A: int, B: int) -> int: 
    ans = 0

    for length in range(len(str(A)), len(str(B))+1): 
        num_list = list(product((4, 7), repeat=length))
        for num in num_list: 
            if A <= int(''.join(map(str, num))) <= B: 
                ans += 1
    
    return ans

    ### ----- joyGo() end ----- ###


if __name__ == "__main__": 
    A, B = map(int, input().split())
    print(joyGo(A, B))


# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, A, B, ans"), 
    [
        (
            1, 
            1, 10, 
            2
        ), 
        (
            2,
            11, 20, 
            0
        ), 
        (
            3, 
            74, 77, 
            2
        ), 
        (
            4, 
            1000000, 5000000, 
            64
        )
    ]
)

def test_joyGo(case_num: int, A: int, B: int, ans: int) -> None: 
    res = joyGo(A, B)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ