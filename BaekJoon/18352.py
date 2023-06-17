# 백준18352 : 특정 거리의 도시 찾기
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(N: int, M: int, K: int, X: int, graph: list) : 
    def dijkstraJoyGo(graph: list, start: int) -> list : 
        dist_list = [sys.maxsize] * len(graph)
        dist_list[start] = 0
        que = [(0, start)]

        while que : 
            dist, u = heappop(que)
            if dist > dist_list[u] : continue
            for v, w in graph[u] : 
                if dist + w < dist_list[v] : 
                    dist_list[v] = dist + w
                    heappush(que, (dist_list[v], v))

        return dist_list


    dist_list = dijkstraJoyGo(graph, X)
    ans_list = [i for i in range(1, N+1) if dist_list[i] == K]
    return ans_list if ans_list else [-1]



if __name__ == "__main__" : 
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) : 
        A, B = map(int, input().split())
        graph[A].append((B, 1))
    
    print(*joyGo(N, M, K, X, graph), sep='\n')