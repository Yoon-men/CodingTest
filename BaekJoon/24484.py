# 백준24484 : 알고리즘 수업 - 깊이 우선 탐색 6
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(node, depth) : 
    visited[node-1] = depth
    global cnt
    visit_order[node-1] = cnt

    for i in graph[node] : 
        if visited[i-1] == -1 : 
            cnt += 1
            DFS(i, depth+1)


if __name__ == "__main__" : 
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    graph = [sorted(i, reverse=True) for i in graph]
    
    visited = [-1] * N
    cnt = 1
    visit_order = [0] * N
    DFS(R-1, 0)

    ans = 0
    for i in range(N) : 
        ans += visited[i]*visit_order[i]
    
    print(ans)