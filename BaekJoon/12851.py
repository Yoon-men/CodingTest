# 백준12851 : 숨바꼭질 2
import sys; input = sys.stdin.readline
from collections import deque
from typing import Tuple

def joyGo(N: int, K: int) -> Tuple[int, int] : 
    dq = deque([N])
    # [걸린 시간, 방법의 수]
    visited = [[-1, 0] for _ in range(10**5 + 1)]
    visited[N] = [0, 1]

    while dq : 
        current = dq.popleft()
            
        for next in (current-1, current+1, current*2) : 
            if 0 <= next <= 10**5 : 
                if visited[next][0] == -1 : 
                    visited[next][0] = visited[current][0] + 1
                    visited[next][1] = visited[current][1]
                    dq.append(next)
                elif visited[next][0] == visited[current][0] + 1 : 
                    visited[next][1] += visited[current][1]
    
    return visited[K]


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    print(*joyGo(N, K), sep='\n')