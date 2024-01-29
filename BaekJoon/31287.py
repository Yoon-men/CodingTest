# 백준31287 : 장난감 강아지
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int, S: str) -> str: 
    x, y = 0, 0
    movings = S * min(N, K)

    for moving in movings: 
        if moving == 'U': 
            y += 1
        elif moving == 'D': 
            y -= 1
        elif moving == 'L': 
            x -= 1
        elif moving == 'R': 
            x += 1

        if (x == 0) and (y == 0): 
            return "YES"
    
    return "NO"


if __name__ == "__main__": 
    N, K = map(int, input().split())
    S = input().strip()

    print(joyGo(N, K, S))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, K, S, ans"), 
    [
        (
            1, 
            4, 2, "URLD", 
            "YES"
        ), 
        (
            2, 
            3, 2, "URD", 
            "NO"
        )
    ]
)

def test_joyGo(case_num: int, N: int, K: int, S: int, ans: str) -> None: 
    res = joyGo(N, K, S)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ