# 백준30224 : Lucky 7
def joyGo(n: int) -> int: 
    if (not '7' in str(n)) and (n % 7 != 0): 
        return 0
    elif (not '7' in str(n)) and (n % 7 == 0): 
        return 1
    elif ('7' in str(n)) and (n % 7 != 0): 
        return 2
    elif ('7' in str(n)) and (n % 7 == 0): 
        return 3


if __name__ == "__main__": 
    n = int(input())
    print(joyGo(n))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, n, ans"), 
    [
        (1, 25, 0), 
        (2, 42, 1), 
        (3, 170, 2), 
        (4, 777, 3), 
        (5, 1, 0), 
        (6, 70, 3)
    ]
)

def test_joyGo(case_num: int, n: int, ans: int) -> None: 
    res = joyGo(n)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ