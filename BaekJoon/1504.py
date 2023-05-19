# 백준1504 : 특정한 최단 경로
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(N: int, E: int, graph: list, v1: int, v2: int) -> int : 
    def dijkstra(graph: list, start: int) : 
        dist = [sys.maxsize for _ in range(N)]
        dist[start] = 0

        pq = [(0, start)]

        while pq : 
            d, u = heappop(pq)
            if d > dist[u] : 
                continue
            for v, w in graph[u] : 
                if dist[u] + w < dist[v] : 
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))

        return dist
    

    start_dist = dijkstra(graph, 0)
    v1_dist = dijkstra(graph, v1)
    v2_dist = dijkstra(graph, v2)

    v1_to_v2 = start_dist[v1] + v1_dist[v2] + v2_dist[N-1]
    v2_to_v1 = start_dist[v2] + v2_dist[v1] + v1_dist[N-1]

    ans = min(v1_to_v2, v2_to_v1)

    return ans if ans < sys.maxsize else -1



if __name__ == "__main__" : 
    N, E = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(E) : 
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    v1, v2 = map(int, input().split())
    v1 -= 1; v2 -= 1
    print(joyGo(N, E, graph, v1, v2))