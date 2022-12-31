# 백준9019 : DSLR
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(inPut, outPut) : 
    q = deque([(inPut, "")])
    visited = [0] * 10000
    while q : 
        n, ans = q.popleft()
        visited[n] = 1
        if n == outPut : 
            return ans

        n2 = (2*n) % 10000
        if not visited[n2] : 
            q.append((n2, ans+"D"))
            visited[n2] = 1

        n2 = 9999 if (n == 0) else n-1
        if not visited[n2] : 
            q.append((n2, ans+"S"))
            visited[n2] = 1

        tmp = str(n).zfill(4)
        n2 = int(tmp[1]+tmp[2]+tmp[3]+tmp[0])
        if not visited[n2] : 
            q.append((n2, ans+"L"))
            visited[n2] = 1

        n2 = int(tmp[3]+tmp[0]+tmp[1]+tmp[2])
        if not visited[n2] : 
            q.append((n2, ans+"R"))
            visited[n2] = 1


if __name__ == "__main__" : 
    for i in range(int(input())) : 
        A, B = map(int, input().split())
        print(joyGo(A, B))