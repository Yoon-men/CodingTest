# 백준2529 : 부등호
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(k: int, Li: List[str]) -> Tuple[str]: 
    LEN_OF_ZERO_TO_NINE = 10

    def chk(a: int, op: str, b: int) -> bool: 
        if op == '>': 
            if a > b: return True
        elif op == '<': 
            if a < b: return True
        
        return False


    def DFS(cnt: int, s: str) -> None: 
        if cnt == k+1: 
            possible_list.append(s)
            return
        
        for i in range(LEN_OF_ZERO_TO_NINE): 
            if visited[i]: continue

            if (cnt == 0) or (chk(int(s[cnt-1]), Li[cnt-1], i)): 
                visited[i] = 1
                DFS(cnt+1, s + str(i))
                visited[i] = 0


    possible_list = []
    visited = [0] * LEN_OF_ZERO_TO_NINE

    DFS(0, '')

    return (possible_list[-1], possible_list[0])



if __name__ == "__main__": 
    k = int(input())
    Li = input().split()

    print(*joyGo(k, Li), sep='\n')



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    "case_num, k, Li, ans", 
    [
        (1, 2, '< >'.split(), ("897", "021")),
        (2, 9, '> < < < > > > < <'.split(), tuple('9567843012\n1023765489'.split('\n')))
    ]
)
def test_joyGo(case_num, k, Li, ans):
    res = joyGo(k, Li)
    assert res == ans, f"Test Case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ
