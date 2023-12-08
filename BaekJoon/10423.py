# 백준10423 : 전기가 부족해
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, M: int, K: int, generators: List[int], graph: List[List[Tuple[int, int]]]) -> int: 
    ans = 0

    visited = [0] * (N+1)

    hq = [(0, generator) for generator in generators]
    while hq: 
        w, u = heappop(hq)
        if not visited[u]: 
            visited[u] = 1
            ans += w
            for v, w in graph[u]: heappush(hq, (w, v))

    return ans



if __name__ == "__main__": 
    N, M, K = map(int, input().split())
    generators = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(M): 
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    print(joyGo(N, M, K, generators, graph))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, K, generators, graph, ans"), 
    [
        (1, 9, 14, 3, [1, 2, 9], [[], [(3, 3), (4, 8)], [(4, 10)], [(1, 3), (4, 11), (5, 6)], [(1, 8), (2, 10), (3, 11), (5, 4), (6, 10)], [(3, 6), (4, 4), (6, 5), (7, 4)], [(4, 10), (5, 5), (7, 7), (8, 4)], [(5, 4), (6, 7), (8, 5), (9, 2)], [(6, 4), (7, 5), (9, 5)], [(7, 2), (8, 5)]], 22), 
        (2, 4, 5, 1, [1], [[], [(2, 5), (3, 5), (4, 5)], [(1, 5), (3, 10)], [(1, 5), (2, 10), (4, 10)], [(1, 5), (3, 10)]], 15), 
        (3, 10, 9, 5, [1, 4, 6, 9, 10], [[], [(2, 3)], [(1, 3), (3, 8)], [(2, 8), (4, 5)], [(3, 5), (5, 1)], [(4, 1), (6, 2)], [(5, 2), (7, 6)], [(6, 6), (8, 3)], [(7, 3), (9, 4)], [(8, 4), (10, 1)], [(9, 1)]], 16)
    ]
)

def test_joyGo(case_num: int, N: int, M: int, K: int, generators: List[int], graph: List[List[Tuple[int, int]]], ans: int) -> None: 
    res = joyGo(N, M, K, generators, graph)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ