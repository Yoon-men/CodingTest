# 백준1753 : 최단경로
import sys; input = sys.stdin.readline
from queue import PriorityQueue

def dijkstraJoyGo(start, graph) : 
    distanceLi = [0 if i == start else sys.maxsize for i in range(len(graph))]
    visited = [0] * len(graph)

    que = PriorityQueue()
    que.put((0, start))         # ((가중치), (목적지))
    while not que.empty() : 
        distance, node = que.get()
        if not visited[node] : 
            visited[node] = 1
            for next_node, weight in graph[node] : 
                total_distance = distance + weight
                if total_distance < distanceLi[next_node] : 
                    distanceLi[next_node] = total_distance
                    que.put((total_distance, next_node))
    
    return distanceLi


if __name__ == "__main__" : 
    V, E = map(int, input().split())
    K = int(input())

    graph = [[] for _ in range(V)]
    for _ in range(E) : 
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
    
    ansLi = dijkstraJoyGo(K-1, graph)

    for ans in ansLi : 
        print("INF" if ans == sys.maxsize else ans)