# 백준21924 : 도시 건설
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, M: int, road_data: List[Tuple[int, int, int]]) -> int: 
    all_w = sum([w for _, _, w in road_data])

    road_list: List[List[Tuple[int, int]]] \
        = [[] for _ in range(N)]
    for u, v, w in road_data: 
        road_list[u-1].append((v-1, w))
        road_list[v-1].append((u-1, w))

    ans = 0

    visited = [0] * N
    hq = [(0, 0)]
    
    while hq: 
        w, u = heappop(hq)

        if not visited[u]: 
            visited[u] = 1
            ans += w
            for v, w in road_list[u]: 
                heappush(hq, (w, v))
    
    return all_w - ans if (sum(visited) == N) else -1



if __name__ == "__main__": 
    N, M = map(int, input().split())
    road_data = [list(map(int, input().split())) for _ in range(M)]
    
    print(joyGo(N, M, road_data))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, road_data, ans"), 
    [
        (
            1, 
            7, 9, 
            [(1, 2, 15), (2, 3, 7), (1, 3, 3), (1, 4, 8), (3, 5, 6), (4, 5, 4), (4, 6, 12), (5, 7, 1), (6, 7, 6)], 
            35
        ), 
        (
            2, 
            8, 10, 
            [(1, 2, 4), (2, 3, 9), (2, 4, 9), (3, 4, 4), (3, 5, 1), (4, 6, 14), (6, 7, 5), (5, 7, 3), (7, 8, 7), (6, 8, 3)], 
            30
        ), 
        (
            3, 
            5, 4, 
            [(1, 2, 1), (2, 3, 1), (3, 1, 1), (4, 5, 5)], 
            -1
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, road_data: List[Tuple[int, int, int]], ans: int) -> None: 
    res = joyGo(N, M, road_data)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ