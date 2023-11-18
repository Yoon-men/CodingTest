# 백준14921 : 용액 합성하기
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, Li: List[int]) -> int: 
    s, e = 0, N-1
    ans = sys.maxsize

    while s < e: 
        _sum = Li[s] + Li[e]
        if abs(_sum) < abs(ans): ans = _sum
        
        if _sum < 0: s += 1
        else: e -= 1
    
    return ans


if __name__ == "__main__": 
    N = int(input())
    Li = list(map(int, input().split()))

    print(joyGo(N, Li))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest
@pytest.mark.parametrize(
    ("case_num, N, Li, ans"), 
    [
        (1, 5, list(map(int, "-101 -3 -1 5 93".split())), 2), 
        (2, 2, list(map(int, "-100000 -99999".split())), -199999), 
        (3, 7, list(map(int, "-698 -332 -123 54 531 535 699".split())), 1)
    ]
)

def test_joyGo(case_num: int, N: int, Li: List[int], ans: int) -> None: 
    res = joyGo(N, Li)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ