# 백준5972 : 택배 배송
import sys; input = sys.stdin.readline
from typing import List, Tuple
from heapq import heappush, heappop

def joyGo(N: int, michi: List[List[Tuple[int, int]]]) -> int : 
    def makeDistanceList(start: int, graph: List[List[Tuple[int, int]]]) -> List[int] : 
        '''Make distance list using dijkstra algorithm.'''
        distance_list = [float("inf")] * len(graph)
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
    

    return makeDistanceList(start=1, graph=michi)[-1]



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    michi = [[] for _ in range(N+1)]
    for _ in range(M) : 
        u, v, w = map(int, input().split())
        michi[u].append((v, w))
        michi[v].append((u, w))

    print(joyGo(N, michi))