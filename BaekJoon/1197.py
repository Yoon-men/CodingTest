# 백준1197 : 최소 스패닝 트리
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(V: int, graph: list[list]) -> int : 
    ans = 0

    visited = [0] * (V+1)
    hq = [(0, 1)]

    while hq : 
        w, u = heappop(hq)
        if not visited[u] : 
            visited[u] = 1
            ans += w
            for v, w in graph[u] : 
                heappush(hq, (w, v))
    
    return ans


if __name__ == "__main__" : 
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E) : 
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    
    print(joyGo(V, graph))