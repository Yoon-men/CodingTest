# 백준24447 : 알고리즘 수업 - 너비 우선 탐색 4
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, M: int, R: int, graph: list) -> None : 
    def BFS(start_node: int) -> list : 
        visited = [0] * N
        cnt = 1
        visited[start_node] = cnt

        depth = [-1] * N
        depth[start_node] = 0

        dq = deque([start_node])
        while dq : 
            start_node = dq.popleft()
            for node in graph[start_node] : 
                if not visited[node] : 
                    cnt += 1
                    visited[node] = cnt
                    depth[node] = depth[start_node] + 1
                    dq.append(node)
        return visited, depth


    graph = [sorted(line) for line in graph]
    visited, depth = BFS(R-1)

    print(sum([visited[i]*depth[i] for i in range(N)]))



if __name__ == "__main__" : 
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    joyGo(N, M, R, graph)