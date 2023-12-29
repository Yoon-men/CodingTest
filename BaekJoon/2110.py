# 백준2110 : 공유기 설치
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, C: int, house_list: List[int]) -> int: 
    house_list.sort()

    s, e = 1, house_list[-1] - house_list[0]
    while s <= e: 
        m = (s + e) // 2
        cur = house_list[0]
        cnt = 1

        for i in range(1, len(house_list)): 
            if house_list[i] >= cur + m: 
                cnt += 1
                cur = house_list[i]
        
        if cnt >= C: 
            s = m + 1
        else: 
            e = m - 1
    
    return s-1


if __name__ == "__main__": 
    N, C = map(int, input().split())
    house_list = [int(input()) for _ in range(N)]

    print(joyGo(N, C, house_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, C, house_list, ans"), 
    [
        (
            1, 
            5, 3, 
            [1, 2, 8, 4, 9], 
            3
        )
    ]
)

def test_joyGo(case_num: int, N: int, C: int, house_list: List[int], ans: int) -> None: 
    res = joyGo(N, C, house_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ