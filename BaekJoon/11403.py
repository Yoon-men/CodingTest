# 백준11403 : 경로 찾기
import sys ; input = sys.stdin.readline

def joyGo(s) : 
    for i in range(N) : 
        if (not visited[i]) and (M[s][i]) : 
            visited[i] = 1
            joyGo(i)

if __name__ == "__main__" : 
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ansM = [[0]*N for _ in range(N)]
    for i in range(N) : 
        joyGo(i)
        for j in range(N) : 
            if visited[j] : ansM[i][j] = 1
        visited = [0] * N

    for i in ansM : 
        print(*i)