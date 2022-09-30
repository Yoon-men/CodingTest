# 백준9372 : 상근이의 여행
import sys ; input = sys.stdin.readline

def joyGo(origin, cnt) : 
    visited[origin] = 1
    for i in Li[origin] : 
        if visited[i]==0 : 
            cnt = joyGo(i, cnt+1)
    return cnt

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        N, M = map(int, input().split())
        Li = [[] for _ in range(N+1)]
        for _ in range(M) : 
            a, b = map(int, input().split())
            Li[a].append(b)
            Li[b].append(a)

        visited = [0]*(N+1)
        ans = joyGo(1, 0)
        print(ans)