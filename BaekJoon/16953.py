# 백준16953 : A → B
from collections import deque

def joyGo(a, b) : 
    q = deque([(a, 0)])
    while q : 
        a, cnt = q.popleft()
        if a == b : 
            return cnt+1

        if a*2 <= b : 
            q.append((a*2, cnt+1))
        if a*10 + 1 <= b : 
            q.append((a*10 + 1, cnt+1))

    return -1

if __name__ == "__main__" : 
    A, B = map(int, input().split())
    print(joyGo(A, B))