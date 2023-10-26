# 백준1238 : 파티
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, X: int, graph: List[Tuple[int, int]]) -> int : 
    def makeDistanceList(start: int, graph: List[Tuple[int, int]]) -> List[int] : 
        '''Make distance list using dijkstra algorithm.'''
        distance_list = [float("inf") for _ in range(len(graph))]
        distance_list[start] = 0

        queue = [(0, start)]
        while queue : 
            current_distance, current_node = heappop(queue)
            if current_distance > distance_list[current_node] : continue

            for next_node, next_distance in graph[current_node] : 
                distance = current_distance + next_distance
                if distance < distance_list[next_node] : 
                    distance_list[next_node] = distance
                    heappush(queue, (distance, next_node))
        
        return distance_list

    
    max_distance = 0
    for i in range(1, N+1) : max_distance = max(max_distance, makeDistanceList(start=i, graph=graph)[X] + makeDistanceList(start=X, graph=graph)[i])
    
    return max_distance



if __name__ == "__main__" : 
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    print(joyGo(N, X, graph))