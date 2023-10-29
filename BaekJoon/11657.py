# 백준11657 : 타임머신
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, graph: List[List[Tuple[int, int]]]) : 
    '''Make distance list using Bellman-Ford algorithm.'''
    distance_list = [float("inf") for _ in range(N)]
    distance_list[0] = 0

    for i in range(N) : 
        for u in range(len(graph)) : 
            for v, w in graph[u] : 
                if (distance_list[u] != float("inf")) and (distance_list[u] + w < distance_list[v]) : 
                    if i == N-1 : return [-1]
                    distance_list[v] = distance_list[u] + w
    
    distance_list = [-1 if (distance == float("inf")) else distance for distance in distance_list]

    return distance_list[1:]



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        A, B, C = map(int, input().split())
        graph[A-1].append((B-1, C))

    print(*joyGo(N, graph), sep='\n')