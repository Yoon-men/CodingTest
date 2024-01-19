# 백준23843 : 콘센트
import sys; input = sys.stdin.readline
from typing import List
from heapq import heapify, heappop

def joyGo(N: int, M: int, needed_time_list: List[int]) -> int: 
    ans = 0

    hq = [-time for time in needed_time_list]
    heapify(hq)

    socket = [heappop(hq) for _ in range(min(N, M))]

    while sum(socket) != 0: 
        for i in range(len(socket)): 
            if socket[i] != 0: 
                socket[i] = socket[i] + 1

            if socket[i] == 0: 
                if hq: socket[i] = heappop(hq)
        
        ans += 1

    return ans


if __name__ == "__main__": 
    N, M = map(int, input().split())
    needed_time_list = list(map(int, input().split()))

    print(joyGo(N, M, needed_time_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, needed_time_list, ans"), 
    [
        (
            1, 
            5, 2, 
            [1, 4, 4, 8, 1], 
            9
        ), 
        (
            2, 
            4, 10, 
            [1, 2, 3, 4], 
            4
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, needed_time_list: List[int], ans: int) -> None: 
    res = joyGo(N, M, needed_time_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ