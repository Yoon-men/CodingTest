# 백준30454 : 얼룩말을 찾아라!
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, L: int, fur_list: List[str]) -> Tuple[int, int]: 
    max_of_black_num, num_of_zebra = 0, 0

    for fur in fur_list: 
        current_black_num = len([i for i in fur.split('0') if i])
        if current_black_num > max_of_black_num: 
            num_of_zebra = 1
            max_of_black_num = current_black_num
        elif current_black_num == max_of_black_num: 
            num_of_zebra += 1

    return (max_of_black_num, num_of_zebra)


if __name__ == "__main__" : 
    N, L = map(int, input().split())
    fur_list = [input().strip() for _ in range(N)]

    print(*joyGo(N, L, fur_list))


# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    "N, L, fur_list, ans", 
    [
        (5, 9, '''110010101
101010100
000011111
011011010
100100101'''.split('\n'), (4, 3))
    ]
)

def test_joyGo(N: int, L: int, fur_list: List[str], ans: Tuple[int, int]): 
    res = joyGo(N, L, fur_list)
    assert res == ans, f"Test Case 1 - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ