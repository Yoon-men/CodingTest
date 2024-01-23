# 백준10804 : 카드 역배치
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(reverse_sections: List[Tuple[int, int]]) -> List[int]: 
    ans = [i for i in range(1, 21)]

    for a, b in reverse_sections: 
        ans = ans[:a-1] + ans[a-1:b][::-1] + ans[b:]

    return ans


if __name__ == "__main__": 
    reverse_sections = [tuple(map(int, input().split())) for _ in range(10)]
    print(*joyGo(reverse_sections))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, reverse_sections, ans"), 
    [
        (
            1, 
            [(5, 10), (9, 13), (1, 2), (3, 4), (5, 6), (1, 2), (3, 4), (5, 6), (1, 20), (1, 20)], 
            [1, 2, 3, 4, 10, 9, 8, 7, 13, 12, 11, 5, 6, 14, 15, 16, 17, 18, 19, 20]
        ), 
        (
            2, 
            [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], 
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        ), 
        (
            3, 
            [(1, 20), (2, 19), (3, 18), (4, 17), (5, 16), (6, 15), (7, 14), (8, 13), (9, 12), (10, 11)], 
            [20, 2, 18, 4, 16, 6, 14, 8, 12, 10, 11, 9, 13, 7, 15, 5, 17, 3, 19, 1]
        )
    ]
)

def test_joyGo(case_num: int, reverse_sections: List[Tuple[int, int]], ans: List[int]) -> None: 
    res = joyGo(reverse_sections)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ