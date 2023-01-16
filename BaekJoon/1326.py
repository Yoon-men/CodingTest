# 백준1326 : 폴짝폴짝
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(a, b) : 
    dq = deque([a])
    visited = [-1] * (N+1)
    visited[a] = 0

    while dq : 
        cur = dq.popleft()
        for i in range(cur, N+1, Li[cur]) : 
            if visited[i] == -1 : 
                dq.append(i)
                visited[i] = visited[cur] + 1
                if i == b : return visited[i]
        for i in range(cur, 0, -Li[cur]) : 
            if visited[i] == -1 : 
                dq.append(i)
                visited[i] = visited[cur] + 1
                if i == b : return visited[i]

    return -1

if __name__ == "__main__" : 
    N = int(input())
    Li = [0] + list(map(int, input().split()))
    a, b = map(int, input().split())

    print(joyGo(a, b))