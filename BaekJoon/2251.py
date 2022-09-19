# 백준2251 : 물통
from collections import deque

def joyGo() : 
    def mung(a, b) : 
        if not visited[a][b] : 
            visited[a][b] = 1
            q.append((a, b))

    q = deque([(0, 0)])
    visited[0][0] = 1
    while q : 
        x, y = q.popleft()
        z = C - x - y
        if x==0 : answer.append(z)

        # from A to B
        water = min(x, B-y)
        mung(x-water, y+water)

        # from A to C
        water = min(x, C-z)
        mung(x-water, y)

        # from B to A
        water = min(A-x, y)
        mung(x+water, y-water)

        # from B to C
        water = min(y, C-z)
        mung(x, y-water)

        # from C to A
        water = min(A-x, z)
        mung(x+water, y)

        # from C to B
        water = min(B-y, z)
        mung(x, y+water)

if __name__ == "__main__" : 
    A, B, C = map(int, input().split())
    visited = [[0]*(B+1) for _ in range(A+1)]
    answer = []
    joyGo()
    print(" ".join(str(i) for i in sorted(answer)))