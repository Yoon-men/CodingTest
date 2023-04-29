# 백준24483 : 알고리즘 수업 - 깊이 우선 탐색 5
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(N: int, M: int, R: int, graph: list) -> None : 
    def DFS(start_node: int) -> None : 
        global visit_cnt
        for node in graph[start_node] : 
            if not visited[node] : 
                visited[node] = visit_cnt
                visit_cnt += 1
                depth[node] = depth[start_node] + 1
                DFS(node)


    graph = [sorted(line) for line in graph]
    visited = [0] * N; visited[R-1] = 1
    global visit_cnt
    visit_cnt = 2
    depth = [-1] * N; depth[R-1] = 0

    DFS(R-1)

    print(sum([visited[i]*depth[i] for i in range(N)]))


if __name__ == "__main__" : 
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    joyGo(N, M, R, graph)