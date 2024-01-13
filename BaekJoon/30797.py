# 백준30797 : 가희와 여행가요
import sys; input = sys.stdin.readline
from typing import List
from heapq import heappush, heappop

def joyGo(n: int, Q: int, road_data: List[List[int]]) -> List[int]: 
    road_list = [[] for _ in range(n+1)]
    for u, v, w, t in road_data: 
        road_list[u].append((v, w, t))
        road_list[v].append((u, w, t))

    cost = 0
    time = 0

    visited = [0] * (n+1)
    hq = [(0, 0, 1)]        # (비용), (시간), (시작 도시 번호)

    while hq: 
        w, t, u = heappop(hq)
        
        if not visited[u]: 
            visited[u] = 1
            cost += w
            time = max(time, t)

            for v, w, t in road_list[u]: 
                heappush(hq, (w, t, v))
    
    return [time, cost] if sum(visited) == n else [-1]



if __name__ == "__main__": 
    n, Q = map(int, input().split())
    road_data = [list(map(int, input().split())) for _ in range(Q)]
    
    print(*joyGo(n, Q, road_data))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, n, Q, road_data, ans"), 
    [
        (
            1, 
            4, 5, 
            [[1, 4, 1, 5], [2, 3, 1, 1000000000], [1, 4, 1, 13], [3, 2, 1, 117], [2, 4, 1, 10]], 
            [117, 3]
        ), 
        (
            2, 
            2, 2, 
            [[1, 2, 5, 1], [2, 1, 3, 2]], 
            [2, 3]
        ), 
        (
            3, 
            5, 1, 
            [[1, 4, 5, 7]], 
            [-1]
        )
    ]
)

def test_joyGo(case_num: int, n: int, Q: int, road_data: List[List[int]], ans: List[int]) -> None: 
    res = joyGo(n, Q, road_data)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ