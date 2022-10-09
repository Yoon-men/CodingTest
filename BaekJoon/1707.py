# 백준1707 : 이분 그래프
import sys ; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def joyGo(element, line) : 
    visited[element] = line
    for i in graph[element] : 
        if not visited[i] : 
            lining = joyGo(i, -line)
            if not lining : return 0
        elif visited[i] == visited[element] : return 0
    return 1

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        V, E = map(int, input().split())
        visited = [0] * (V+1)
        graph = [[] for _ in range(V+1)]
        for _ in range(E) : 
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, V+1) : 
            if not visited[i] : 
                res = joyGo(i, 1)
                if not res : break

        print("YES" if res else "NO")