# 백준2644 : 촌수계산
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(node) : 
    node -= 1
    for i in graph[node] : 
        if not visited[i-1] : 
            visited[i-1] = visited[node] + 1
            joyGo(i)

if __name__ == "__main__" : 
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    visited = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(m) : 
        u, v = map(int, input().split())
        graph[u-1].append(v)
        graph[v-1].append(u)
    
    joyGo(a)

    print(visited[b-1] if (visited[b-1] > 0) else -1)