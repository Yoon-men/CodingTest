# 백준1446 : 지름길
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstraJoyGo(graph, start) : 
    distanceLi = [sys.maxsize] * len(graph)
    distanceLi[start] = 0
    que = [(0, start)]

    while que : 
        distance, node = heappop(que)

        if distance > distanceLi[node] : continue

        for next_node, weight in graph[node] : 
            total_distance = distance + weight
            if total_distance < distanceLi[next_node] : 
                distanceLi[next_node] = total_distance
                heappush(que, (total_distance, next_node))
    
    return distanceLi


if __name__ == "__main__" : 
    N, D = map(int, input().split())

    graph = [[] for _ in range(D+1)]
    for i in range(D) : 
        graph[i].append((i+1, 1))

    for _ in range(N) : 
        u, v, w = map(int, input().split())
        if v > D : continue
        graph[u].append((v, w))

    ansLi = dijkstraJoyGo(graph, 0)

    print(ansLi[D])