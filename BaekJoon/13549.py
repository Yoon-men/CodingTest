# 백준13549 : 숨바꼭질 3
from collections import deque

def joyGo(N: int, K: int) -> int : 
    dq = deque([N])
    visited = [-1] * (10**5 + 1)
    visited[N] = 0
    while dq : 
        current = dq.popleft()
        if current == K : return visited[current]

        for next in (current-1, current+1, current*2) : 
            if (0 <= next <= 10**5) and (visited[next] == -1) : 
                if next == current*2 : 
                    visited[next] = visited[current]
                    dq.appendleft(next)
                else : 
                    visited[next] = visited[current] + 1
                    dq.append(next)


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    print(joyGo(N, K))