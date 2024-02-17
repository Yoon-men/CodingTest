# 백준23925 : Retype
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int, S: int) -> int: 
    a, b = K-1, K-1

    a += 1
    a += N

    b += K-S
    b += N-S+1

    return min(a, b)


if __name__ == "__main__": 
    for i in range(int(input())): 
        N, K, S = map(int, input().split())
        print(f"Case #{i+1}: {joyGo(N, K, S)}")



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, K, S, ans"), 
    [
        (
            1, 
            10, 5, 2, 
            15
        ), 
        (
            2, 
            10, 7, 6, 
            12
        )
    ]
)

def test_joyGo(case_num: int, N: int, K: int, S: int, ans: int) -> None: 
    res = joyGo(N, K, S)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ