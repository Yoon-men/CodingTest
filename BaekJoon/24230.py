# 백준24230 : 트리 색칠하기
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, paint: list, graph: list) -> int : 
    def BFS(node: int) -> int : 
        dq = deque([node])
        visited[node] = 1

        ans = 0
        while dq : 
            node = dq.popleft()
            for next in graph[node] : 
                if not visited[next] : 
                    visited[next] = 1
                    dq.append(next)
                    if paint[node] != paint[next] : 
                        ans += 1
        
        return ans


    global ans
    visited = [0] * N
    ans = BFS(0)
    if paint[0] != 0 : ans += 1

    return ans



if __name__ == "__main__" : 
    N = int(input())
    paint = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(N-1) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    print(joyGo(N, paint, graph))