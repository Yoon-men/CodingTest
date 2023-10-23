# 백준1647 : 도시 분할 계획
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, graph: List[List[Tuple[int, int]]]) -> int : 
    ans = 0
    hq = [(0, 1)]
    visited = [0] * (N+1)
    money_pit = 0
    while hq : 
        w, u = heappop(hq)
        if not visited[u] : 
            visited[u] = 1
            ans += w
            money_pit = max(money_pit, w)
            for v, w in graph[u] : heappush(hq, (w, v))
    
    return ans - money_pit


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    
    print(joyGo(N, graph))