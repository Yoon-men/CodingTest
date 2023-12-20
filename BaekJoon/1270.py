# 백준1270 : 전쟁 - 땅따먹기
import sys; input = sys.stdin.readline
from typing import List, Union
from collections import Counter

def joyGo(land_list: List[int]) -> Union[int, str]: 
    cnt_dict = Counter(land_list[1:])
    max_key, max_value = cnt_dict.most_common()[0]

    return max_key if (max_value > land_list[0]//2) \
                    else "SYJKGW"


if __name__ == "__main__": 
    for _ in range(int(input())): 
        land_list = list(map(int, input().split()))
        print(joyGo(land_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, land_list, ans"), 
    [
        (1, list(map(int, "10 1 2 3 1 2 3 1 2 3 1".split())), "SYJKGW"), 
        (2, list(map(int, "5 1 1 1 2 2".split())), 1), 
        (3, list(map(int, "6 10 10 2 10 10 2".split())), 10), 
        (4, list(map(int, "6 1 1 1 2 2 2 ".split())), "SYJKGW")
    ]
)

def test_joyGo(case_num: int, land_list: List[int], ans: int) -> None: 
    res = joyGo(land_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ