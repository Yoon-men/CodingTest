# 백준1940 : 주몽
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, M: int, nums: List[int]) -> int: 
    nums.sort()

    ans = 0

    for i in range(N-1): 
        for j in range(i+1, N): 
            if nums[i] + nums[j] == M: 
                ans += 1
                break
    
    return ans


if __name__ == "__main__": 
    N = int(input())
    M = int(input())
    nums = list(map(int, input().split()))

    print(joyGo(N, M, nums))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, nums, ans"), 
    [
        (
            1, 
            6, 9, 
            [2, 7, 4, 1, 5, 3], 
            2
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, nums: List[int], ans: int) -> None: 
    pass                # Test code / please delete this line.
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ