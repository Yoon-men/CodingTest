# 백준7576 : 토마토
from collections import deque
import sys
input = sys.stdin.readline

def bfs() : 
    while q : 
        y, x = q.popleft()
        for i in range(4) : 
            near_Y = y + around_Y[i]
            near_X = x + around_X[i]
            if (0 <= near_Y < N) and (0 <= near_X < M) and (graph[near_Y][near_X] == 0) : 
                q.append([near_Y, near_X])
                graph[near_Y][near_X] = graph[y][x] + 1

if __name__ == "__main__" : 
    M, N = map(int, input().split())
    graph = [[] for _ in range(N)]
    q = deque()
    for i in range(N) : 
        graph[i] = list(map(int, input().split()))
        for j in range(M) : 
            if graph[i][j] == 1 : 
                q.append([i, j])
    around_Y = [0, 0, 1, -1]
    around_X = [-1, 1, 0, 0]
    bfs()
    def result() : 
        answer = 0
        for i in graph : 
            for j in i : 
                if j == 0 : 
                    return -1
                answer = max(answer, j)
        return answer-1
    print(result())