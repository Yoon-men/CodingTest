# 백준24479 : 알고리즘 수업 - 깊이 우선 탐색 1
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(N: int, M: int, R: int, graph: list) -> None : 
    def DFS(start_node: int) -> None : 
        global cnt
        visited[start_node] = cnt
        for node in graph[start_node] : 
            if not visited[node] : 
                cnt += 1
                DFS(node)

    visited = [0] * N
    graph = [sorted(line) for line in graph]
    global cnt
    cnt = 1
    DFS(R-1)

    print("\n".join(map(str, visited)))



if __name__ == "__main__" : 
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    joyGo(N, M, R, graph)