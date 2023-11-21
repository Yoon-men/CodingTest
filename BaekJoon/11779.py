# 백준11779 : 최소비용 구하기 2
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(n: int, m: int, graph: List[List[Tuple[int, int]]], s: int, e: int) -> Tuple[int, int, List[int]]: 
    parent_list = [-1] * (n+1)
    distance_list = [sys.maxsize] * (n+1)
    distance_list[s] = 0
    hq = [(0, s)]
    while hq: 
        current_w, u = heappop(hq)
        if current_w > distance_list[u]: continue

        for v, next_w in graph[u]: 
            w = current_w + next_w
            if distance_list[v] > w: 
                distance_list[v] = w
                parent_list[v] = u
                heappush(hq, (w, v))

    route_list = []
    current = e
    while current != s: 
        route_list.append(current)
        current = parent_list[current]
    route_list.append(s)
    route_list.reverse()
    
    return (distance_list[e], len(route_list), route_list)


if __name__ == "__main__": 
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m): 
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    s, e = map(int, input().split())
    
    w, route_len, route_list = joyGo(n, m, graph, s, e)
    print(w)
    print(route_len)
    print(*route_list)



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("n, m, graph, s, e, ans"), 
    [
        (5, 8, [[], [(2, 2), (3, 3), (4, 1), (5, 10)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []], 1, 5, (4, 3, [1, 3, 5]))
    ]
)

def test_joyGo(n: int, m: int, graph: List[List[Tuple[int, int]]], s: int, e: int, ans: Tuple[int, int, List[int]]) -> None: 
    res = joyGo(n, m, graph, s, e)
    assert res == ans, f"Test case 1 - 틀렸습니다. (your result: {res} / ans: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ