# 백준6119 : 숨바꼭질
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop
from collections import Counter

def joyGo(N: int, M: int, graph: List[List[int]]) -> Tuple[int, int, int]: 
    distance_list = [sys.maxsize for _ in range(N+1)]
    distance_list[1] = 0

    queue = [(0, 1)]
    while queue: 
        crt_distance, crt_node = heappop(queue)
        if crt_distance > distance_list[crt_node]: 
            continue

        for nxt_node in graph[crt_node]: 
            distance = crt_distance + 1
            if distance < distance_list[nxt_node]: 
                distance_list[nxt_node] = distance
                heappush(queue, (distance, nxt_node))
    
    distance_list = [-1 if (distance == sys.maxsize) else distance for distance in distance_list]
    
    return (distance_list.index(max(distance_list)), \
                max(distance_list), \
                    Counter(distance_list)[max(distance_list)])


if __name__ == "__main__": 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M): 
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    
    print(*joyGo(N, M, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("N, M, graph, ans"), 
    [
        (6, 7, [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]], (4, 2, 3))
    ]
)

def test_joyGo(N: int, M: int, graph: List[List[int]], ans: Tuple[int, int, int]) -> None: 
    res = joyGo(N, M, graph)
    assert res == ans, f"Test case - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ