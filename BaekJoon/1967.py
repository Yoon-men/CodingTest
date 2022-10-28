# 백준1967 : 트리의 지름
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(s) : 
    visited = [0] * (n+1)
    dq = deque([s])
    visited[s] = 1
    result= [0, 0]

    while dq : 
        p = dq.popleft()
        for l, d in graph[p] : 
            if not visited[l] : 
                visited[l] = visited[p] + d
                dq.append(l)
                if result[0] < visited[l] : result = [visited[l], l]
    
    result[0] -= 1
    return result

if __name__ == "__main__" : 
    n = int(input())
    if n == 1 : 
        print(0)
    else : 
        graph = [[] for _ in range(n+1)]
        for _ in range(n-1) : 
            p, c, d= map(int, input().split())
            graph[p].append((c, d))
            graph[c].append((p, d))

        _, node = joyGo(1)
        distance, _ = joyGo(node)
        print(distance)