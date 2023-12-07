# 백준15655 : N과 M (6)
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, M: int, nums: List[int]) -> List[List[int]]: 
    def dfs(depth: int, start_idx: int) -> None: 
        if depth == M: 
            ans.append(tmp[::])
            return
        
        for idx in range(start_idx, N): 
            tmp.append(nums[idx])
            dfs(depth+1, idx+1)
            tmp.pop()
        
        return


    nums.sort()
    tmp, ans = [], []

    dfs(depth=0, start_idx=0)

    return ans



if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    ans_list = joyGo(N, M, nums)
    for row in ans_list: 
        print(*row)



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, nums, ans"), 
    [
        (1, 3, 1, [4, 5, 2], [[2], [4], [5]]),
        (2, 4, 2, [9, 8, 7, 1], [[1, 7], [1, 8], [1, 9], [7, 8], [7, 9], [8, 9]]),
        (3, 4, 4, [1231, 1232, 1233, 1234], [[1231, 1232, 1233, 1234]])
    ]
)

def test_joyGo(case_num: int, N: int, M: int, nums: list, ans: list) -> None: 
    res = joyGo(N, M, nums)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ