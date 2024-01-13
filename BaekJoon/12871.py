# 백준12871 : 무한 문자열
import sys; input = sys.stdin.readline

def joyGo(s: str, t: str) -> int: 
    return 1 if s * len(t) == t * len(s) else 0


if __name__ == "__main__": 
    print(joyGo(input(), input()))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, s, t, ans"), 
    [
        (
            1, 
            "ab", "abab", 
            1
        ), 
        (
            2, 
            "abc", "bca", 
            0
        )
    ]
)

def test_joyGo(case_num: int, s: str, t: str, ans: int) -> None: 
    res = joyGo(s, t)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ