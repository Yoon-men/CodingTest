# 백준12101 : 1, 2, 3 더하기 2
import sys; input = sys.stdin.readline
from typing import List

def joyGo(n: int, k: int) -> str: 
    def DFS(num: int, formula: List[int]) -> None: 
        if num == n: 
            formula_list.append(formula)
            return

        if num + 1 <= n: 
            DFS(num+1, formula+[1])
        if num + 2 <= n: 
            DFS(num+2, formula+[2])
        if num + 3 <= n: 
            DFS(num+3, formula+[3])


    formula_list = []
    DFS(0, [])

    return '+'.join(map(str, formula_list[k-1])) if (k <= len(formula_list)) else "-1"



if __name__ == "__main__": 
    n, k = map(int, input().split())
    
    print(joyGo(n, k))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, n, k, ans"), 
    [
        (1, 4, 3, "1+2+1"), 
        (2, 4, 5, "2+1+1"), 
        (3, 4, 7, "3+1"), 
        (4, 4, 8, "-1")
    ]
)

def test_joyGo(case_num: int, n: int, k: int, ans: str) -> None: 
    res = joyGo(n, k)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ