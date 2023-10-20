# 백준1922 : 네트워크 연결
import sys; input = sys.stdin.readline
from typing import List
from heapq import heappush, heappop

def joyGo(N: int, graph: List[List[int]]) -> int : 
    ans = 0

    visited = [0] * (N+1)
    hq = [(0, 1)]
    while hq : 
        w, u = heappop(hq)
        if not visited[u] : 
            ans += w
            visited[u] = 1
            for v, w in graph[u] : heappush(hq, (w, v))

    return ans


if __name__ == "__main__" : 
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(joyGo(N, graph))