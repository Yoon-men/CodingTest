# 백준20160 : 야쿠르트 아줌마 야쿠르트 주세요
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(V: int, E: int, graph: List[List[Tuple[int, int]]], yakult_moving: List[int], start: int) -> int: 
    def makeDistanceList(start: int) -> List[int]: 
        dist_list = [0 if i == start else sys.maxsize for i in range(V+1)]

        hq = [(0, start)]
        while hq: 
            current_dist, current_node = heappop(hq)

            if current_dist > dist_list[current_node]: continue

            for next_node, next_dist in graph[current_node]: 
                dist = current_dist + next_dist
                if dist_list[next_node] > dist: 
                    dist_list[next_node] = dist
                    heappush(hq, (dist, next_node))

        return dist_list
    
        ### ----- makeDistanceList() end ----- ###

    
    dist_for_me = makeDistanceList(start)
    
    moving_of_mrs = yakult_moving[0]

    ans = sys.maxsize
    total_dist = 0
    for nextYakult in yakult_moving: 
        dist_for_mrs = makeDistanceList(moving_of_mrs)

        if dist_for_mrs[nextYakult] == sys.maxsize: 
            continue

        total_dist += dist_for_mrs[nextYakult]
        if total_dist >= dist_for_me[nextYakult]: 
            ans = min(ans, nextYakult)

        moving_of_mrs = nextYakult
    
    return -1 if ans == sys.maxsize else ans

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E): 
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    yakult_moving = list(map(int, input().split()))
    start = int(input())
    
    print(joyGo(V, E, graph, yakult_moving, start))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, V, E, graph, yakult_moving, start, ans"), 
    [
        (
            1, 
            5, 5, 
            [[], [(2, 1), (4, 1)], [(1, 1), (3, 1), (3, 1)], [(2, 1), (2, 1), (4, 1)], [(1, 1), (3, 1)], []], 
            [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 
            5, 
            -1
        ), 
        (
            2, 
            6, 5, 
            [[], [(2, 1)], [(1, 1), (3, 10)], [(2, 10), (4, 100)], [(3, 100), (5, 1000)], [(4, 1000), (6, 10000)], [(5, 10000)]], 
            [1, 2, 1, 2, 1, 2, 6, 5, 4, 3], 
            6, 
            3
        ), 
        (
            3, 
            11, 15, 
            [[], [(6, 76), (9, 839), (6, 398), (8, 159)], [(8, 638), (3, 84)], [(4, 715), (4, 961), (7, 723), (2, 84), (10, 943)], [(3, 715), (3, 961), (6, 556)], [(11, 55), (8, 663)], [(1, 76), (7, 89), (1, 398), (4, 556)], [(6, 89), (9, 847), (3, 723)], [(5, 663), (2, 638), (1, 159)], [(7, 847), (1, 839)], [(3, 943)], [(5, 55)]],
            [i for i in range(1, 11)], 
            10, 
            5
        )
    ]
)

def test_joyGo(case_num: int, V: int, E: int, graph: List[List[Tuple[int, int]]], yakult_moving: List[int], start: int, ans: int) -> None: 
    res = joyGo(V, E, graph, yakult_moving, start)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ