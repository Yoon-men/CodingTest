# 백준9342 : 염색체
import sys; input = sys.stdin.readline
import re

def joyGo(string: str) -> str: 
    return "Good" if re.match("^[A-F]?A+F+C+[A-F]?$", string) == None else "Infected!"


if __name__ == "__main__": 
    for _ in range(int(input())): 
        print(joyGo(input().strip()))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

input_datas = '''AFC
AAFC
AAAFFCC
AAFCC
BAFC
QWEDFGHJMNB
DFAFCB
ABCDEFC
DADC
SDFGHJKLQWERTYU
AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFC
AAAFFFFFBBBBCCCAAAFFFF
ABCDEFAAAFFFCCCABCDEF
AFCP
AAFFCPP'''.split('\n')

ans_datas = '''Infected!
Infected!
Infected!
Infected!
Infected!
Good
Good
Good
Good
Good
Good
Good
Good
Good
Good'''.split('\n')

@pytest.mark.parametrize(
    ("case_num, string, ans"), 
    [(i+1, input_datas[i], ans_datas[i]) for i in range(len(input_datas))]
)

def test_joyGo(case_num: int, string: str, ans: str) -> None: 
    res = joyGo(string)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ