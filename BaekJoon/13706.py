# 백준13706 : 제곱근
def joyGo(N: int) -> int: 
    s, e = 1, N
    while s <= e: 
        m = (s + e) // 2

        if m**2 == N: 
            return m
        elif m**2 < N: 
            s = m + 1
        else: 
            e = m - 1
    
    return s

    ### ----- joyGo() end ----- ###


if __name__ == "__main__": 
    N = int(input())
    print(joyGo(N))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, ans"), 
    [
        (1, 36, 6), 
        (2, 81, 9), 
        (3, 226576, 476)
    ]
)

def test_joyGo(case_num: int, N: int, ans: int) -> None: 
    res = joyGo(N)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ