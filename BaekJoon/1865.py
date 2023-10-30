# 백준1865 : 웜홀
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, graph: List[List[Tuple]]) -> str : 
    def makeDistanceList(start: int) -> List[int] : 
        '''Make distance list using Bellman-Ford algorithm.'''
        distance_list = [sys.maxsize for _ in range(N)]
        distance_list[start] = 0

        for i in range(N) : 
            for u in range(N) : 
                for v, w in graph[u] : 
                    if distance_list[u] + w < distance_list[v] : 
                        if i == N-1 : return [-1]
                        distance_list[v] = distance_list[u] + w
        
        return distance_list

    
    return "YES" if (makeDistanceList(start=0) == [-1]) else "NO"



if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        N, M, W = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(M) : 
            S, E, T = map(int, input().split())
            graph[S-1].append((E-1, T))
            graph[E-1].append((S-1, T))
        for _ in range(W) : 
            S, E, T = map(int, input().split())
            graph[S-1].append((E-1, -T))
        print(joyGo(N, graph))