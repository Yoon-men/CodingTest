# 백준5014 : 스타트링크
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(s, e) : 
    dq = deque([s])
    visited = [-1] * (F+1)
    visited[s] = 0

    while dq : 
        cur = dq.popleft()
        if cur == e : return visited[cur]

        for i in (cur+U, cur-D) : 
            if (0 < i <= F) and (visited[i] == -1) : 
                dq.append(i)
                visited[i] = visited[cur] + 1

    return "use the stairs"


if __name__ == "__main__" : 
    F, S, G, U, D = map(int, input().split())
    print(joyGo(S, G))