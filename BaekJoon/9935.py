# 백준9935 : 문자열 폭발
import sys; input = sys.stdin.readline

def joyGo(string: str, bakuhatsu: str) -> str: 
    stack = []

    bakuhatsu = list(bakuhatsu)

    for s in string: 
        stack.append(s)
        if stack[len(stack) - len(bakuhatsu):] == bakuhatsu: 
            for _ in range(len(bakuhatsu)): 
                stack.pop()

    if stack: 
        return ''.join(stack)
    else: 
        return "FRULA"


if __name__ == "__main__": 
    string = input().strip()
    bakuhatsu = input().strip()

    print(joyGo(string, bakuhatsu))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, string, bakuhatsu, ans"), 
    [
        (
            1, 
            "mirkovC4nizCC44", "C4", 
            "mirkovniz"
        ), 
        (
            2, 
            "12ab112ab2ab", "12ab", 
            "FRULA"
        )
    ]
)

def test_joyGo(case_num: int, string: str, bakuhatsu: str, ans: str) -> None: 
    res = joyGo(string, bakuhatsu)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ