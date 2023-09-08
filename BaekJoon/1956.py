# 백준1956 : 운동
import sys; input = sys.stdin.readline
from typing import Tuple

def joyGo(V: int, E: int, road_info: Tuple[Tuple[int, int, int]]) -> int : 
    graph = [[sys.maxsize]*(V+1) for _ in range(V+1)]
    for u, v, w in road_info : graph[u][v] = w

    for k in range(1, V+1) : 
        for i in range(1, V+1) : 
            for j in range(1, V+1) : 
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    
    ans = sys.maxsize
    for i in range(1, V+1) : 
        ans = min(graph[i][i], ans)
    
    return -1 if (ans == sys.maxsize) else ans


if __name__ == "__main__" : 
    V, E = map(int, input().split())
    road_info = tuple(tuple(map(int, input().split())) for _ in range(E))

    print(joyGo(V, E, road_info))