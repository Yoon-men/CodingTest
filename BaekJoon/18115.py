# 백준18115 : 카드 놓기
import sys; input = sys.stdin.readline
from typing import List
from collections import deque

def joyGo(N: int, skill_list: List[int]) -> str: 
    skill_list.reverse()
    ans = deque()

    for i in range(N): 
        if skill_list[i] == 1: 
            ans.appendleft(i+1)
        elif skill_list[i] == 2: 
            ans.insert(1, i+1)
        else: 
            ans.append(i+1)
    
    return ' '.join(map(str, ans))



if __name__ == "__main__": 
    N = int(input())
    skill_list = list(map(int, input().split()))

    print(joyGo(N, skill_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, skill_list, ans"), 
    [
        (
            1, 
            5, [1,1,1,1,1], 
            "5 4 3 2 1"
        ), 
        (
            2, 
            5, [2,3,3,2,1], 
            "1 5 2 3 4"
        )
    ]
)

def test_joyGo(case_num: int, N: int, skill_list: List[int], ans: List[int]) -> None: 
    res = joyGo(N, skill_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ