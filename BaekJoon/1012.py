# 백준1012 : 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(y, x) : 
    graph[y][x] = 0
    for i in range(4) : 
        near_Y = y + around_Y[i]
        near_X = x + around_X[i]
        if (0 <= near_Y < N) and (0 <= near_X < M) : 
            if graph[near_Y][near_X] == 1 : 
                graph[near_Y][near_X] = 0
                dfs(near_Y, near_X)

if __name__ == "__main__" : 
    around_Y = [0, 0, 1, -1]
    around_X = [-1, 1, 0, 0]

    for _ in range(int(input())) : 
        answer = 0
        M, N, K = map(int, input().split())
        graph = [[0]*M for i in range(N)]
        for __ in range(K) : 
            X, Y = map(int, input().split())
            graph[Y][X] = 1
        for i in range(N) : 
            for j in range(M) : 
                if graph[i][j] == 1 : 
                    dfs(i, j)
                    answer += 1
        print(answer)