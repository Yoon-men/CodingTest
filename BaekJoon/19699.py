# 백준19699 : 소-난다!
import sys; input = sys.stdin.readline
from typing import List
from itertools import combinations

def joyGo(N: int, M: int, weight_list: List[int]) -> List[int]: 
    def is_prime(num: int) -> bool: 
        for i in range(2, int(num**0.5)+1): 
            if num % i == 0: return False
        return True


    ans = []

    comb_list = list(combinations(weight_list, M))
    for comb in comb_list: 
        if is_prime(sum(comb)): 
            ans.append(sum(comb))
    
    return sorted(set(ans)) if ans else [-1]



if __name__ == "__main__": 
    N, M = map(int, input().split())
    weight_list = list(map(int, input().split()))

    print(*joyGo(N, M, weight_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, weight_list, ans"), 
    [
        (
            1, 
            5, 3, 
            [2, 4, 10, 5, 8], 
            [11, 17, 19, 23]
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, weight_list: List[int], ans: List[int]) -> None: 
    res = joyGo(N, M, weight_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ