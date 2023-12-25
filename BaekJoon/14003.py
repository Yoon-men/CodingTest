# 백준14003 : 가장 긴 증가하는 부분 수열 5
import sys; input = sys.stdin.readline
from typing import List, Tuple
from bisect import bisect_left

def joyGo(N: int, num_list: List[int]) -> Tuple[int, List[int]]: 
    # def getPosition(num: int) -> int: 
    #     s, e = 0, len(lis_list)-1
    #     while s <= e: 
    #         m = (s + e) // 2
    #         if lis_list[m] == num: 
    #             return m
    #         elif lis_list[m] < num: 
    #             s = m + 1
    #         else: 
    #             e = m - 1
        
    #     return s
        
    #     ### ----- getPosition() end ----- ###

    lis_list = [num_list[0]]
    dp = [(0, num_list[0])]

    for i in range(1, N): 
        if num_list[i] > lis_list[-1]: 
            lis_list.append(num_list[i])
            dp.append((len(lis_list) - 1, num_list[i]))
        else: 
            # position = getPosition(num_list[i])
            position = bisect_left(lis_list, num_list[i])
            lis_list[position] = num_list[i]
            dp.append((position, num_list[i]))
    
    result_list = [-1] * len(lis_list)
    last_position = len(lis_list) - 1
    for i in range(len(dp)-1, -1, -1): 
        if dp[i][0] == last_position: 
            result_list[dp[i][0]] = dp[i][1]
            last_position -= 1
    
    return (len(lis_list), result_list)

    ### ----- joyGo() end ----- ###


if __name__ == "__main__": 
    N = int(input())
    num_list = list(map(int, input().split()))

    ans = joyGo(N, num_list)
    print(ans[0])
    print(*ans[1])



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, num_list, ans"), 
    [
        (1, 6, list(map(int, "10 20 10 30 20 50".split())), (4, [10, 20, 30, 50])), 
        (2, 16, list(map(int, "-60 -41 -100 8 -8 -52 -62 -61 -76 -52 -52 14 -11 -2 -54 46".split())), (7, list(map(int, "-100 -62 -61 -52 -11 -2 46".split())))), 
        (3, 3, [-1, 0, 1], (3, [-1, 0, 1]))
    ]
)

def test_joyGo(case_num: int, N: int, num_list: List[int], ans: Tuple[int, List[int]]) -> None: 
    res = joyGo(N, num_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ