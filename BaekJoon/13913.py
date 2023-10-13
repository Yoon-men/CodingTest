# 백준13913 : 숨바꼭질 4
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, K: int) -> None : 
    dq = deque([N])
    visited = [-1] * (10**5 + 1)
    visited[N] = 0
    previous = [-1] * (10**5 + 1)
    while dq : 
        current = dq.popleft()
        if current == K : 
            print(visited[K])
            moving = [K]
            tmp = K
            while tmp != N : 
                moving.append(previous[tmp])
                tmp = previous[tmp]
            print(*moving[::-1])

        for next in (current-1, current+1, current*2) : 
            if (0 <= next <= 10**5) and (visited[next] == -1) : 
                visited[next] = visited[current] + 1
                previous[next] = current
                dq.append(next)


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    joyGo(N, K)