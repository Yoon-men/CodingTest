# 백준15961 : 회전 초밥
import sys; input = sys.stdin.readline
from typing import List
from collections import defaultdict

def joyGo(N: int, d: int, k: int, c: int, sushi_list: List[int]) -> int: 
    ans = 0

    sushi_dict = defaultdict(int)
    sushi_dict[c] += 1
    for sushi_kind in sushi_list[:k]: sushi_dict[sushi_kind] += 1

    sushi_list.extend(sushi_list[:k])
    for i in range(k, len(sushi_list)): 
        ans = max(ans, len(sushi_dict))

        prev_sushi = sushi_list[i-k]
        sushi_kind = sushi_list[i]

        sushi_dict[prev_sushi] -= 1
        if not sushi_dict[prev_sushi]: del sushi_dict[prev_sushi]

        sushi_dict[sushi_kind] += 1

    return ans


if __name__ == "__main__": 
    N, d, k, c = map(int, input().split())
    sushi_list = [int(input()) for _ in range(N)]

    print(joyGo(N, d, k, c, sushi_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, d, k, c, sushi_list, ans"),  
    [
        (1, 8, 30, 4, 30, [7, 9, 7, 30, 2, 7, 9, 25], 5), 
        (2, 8, 50, 4, 7, [2, 7, 9, 25, 7, 9, 7, 30], 4)
    ]
)

def test_joyGo(case_num: int, N: int, d: int, k: int, c: int, sushi_list: List[int], ans: int): 
    res = joyGo(N, d, k, c, sushi_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ