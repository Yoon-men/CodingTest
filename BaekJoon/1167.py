# 백준1167 : 트리의 지름
import sys ; input = sys.stdin.readline
from collections import deque

def joyGo(s) : 
    visited = [0] * (V+1)
    dq = deque([s])
    visited[s] = 1
    result = [0, 0]

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
    V = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(V) : 
        info = list(map(int, input().split()))
        for i in range(1, len(info)-2, 2) : 
            graph[info[0]].append((info[i], info[i+1]))

    _, node = joyGo(1)
    distance, _ = joyGo(node)
    print(distance)