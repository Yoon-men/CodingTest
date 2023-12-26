# 백준16398 : 행성 연결
import sys; input = sys.stdin.readline
from typing import List
from heapq import heappush, heappop

def joyGo(N: int, cost_matrix: List[List[int]]) -> int: 
    ans = 0
    
    visited = [0] * N
    hq = [(0, 0)]
    while hq: 
        w, u = heappop(hq)
        if not visited[u]: 
            ans += w
            visited[u] = 1
            for v, w in enumerate(cost_matrix[u]): 
                if w: 
                    heappush(hq, (w, v))

    return ans


if __name__ == "__main__": 
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]
    print(joyGo(N, cost_matrix))


# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, cost_matrix, ans"), 
    [
        (
            1, 
            3, [[0, 2, 3], [2, 0, 1], [3, 1, 0]], 3
        ), 
        (
            2, 
            5, [[0, 6, 8, 1, 3], [6, 0, 5, 7, 3], [8, 5, 0, 9, 4], [1, 7, 9, 0, 6], [3, 3, 4, 6, 0]], 11
        )
    ]
)

def test_joyGo(case_num: int, N: int, cost_matrix: List[List[int]], ans: int) -> None: 
    res = joyGo(N, cost_matrix)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ