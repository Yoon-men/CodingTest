# 백준3986 : 좋은 단어
import sys; input = sys.stdin.readline
from typing import List

def joyGo(words: List[str]) -> int: 
    ans = 0

    for word in words: 
        stack = []

        for char in word: 
            if stack and (stack[-1] == char): 
                stack.pop()
            else: 
                stack.append(char)

        if not stack: 
            ans += 1

    return ans


if __name__ == "__main__": 
    words = [input().strip() for _ in range(int(input()))]

    print(joyGo(words))


# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, words, ans"), 
    [
        (
            1, 
            ['ABAB', 'AABB', 'ABBA'], 
            2
        ), 
        (
            2, 
            ['AAA', 'AA', 'AB'], 
            1
        ), 
        (
            3, 
            ['ABBABB'], 
            1
        ), 
        (
            4, 
            ['ABABBABA', 'ABBBABAABABA'], 
            2
        )
    ]
)

def test_joyGo(case_num: int, words: List[str], ans: int) -> None: 
    res = joyGo(words)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ