# 백준7569 : 토마토
from collections import deque
import sys
input = sys.stdin.readline

def bfs() : 
    while q : 
        z, y, x = q.popleft()
        for i in range(6) : 
            near_Z = z + around_Z[i]
            near_Y = y + around_Y[i]
            near_X = x + around_X[i]
            if (0 <= near_Z < H) and (0 <= near_Y < N) and (0 <= near_X < M) and (graph[near_Z][near_Y][near_X] == 0) : 
                q.append([near_Z, near_Y, near_X])
                graph[near_Z][near_Y][near_X] = graph[z][y][x] + 1

if __name__ == "__main__" : 
    M, N, H = map(int, input().split())
    graph = [[]for _ in range(H)]
    q = deque()
    for i in range(H) : 
        temp = [[] for _ in range(N)]
        for j in range(N) : 
            temp[j] = list(map(int, input().split()))
            for k in range(M) : 
                if temp[j][k] == 1 : 
                    q.append([i, j, k])
        graph[i] = temp
    around_Z = [0, 0, 0, 0, 1, -1]
    around_Y = [0, 0, 1, -1, 0, 0]
    around_X = [-1, 1, 0, 0, 0, 0]
    bfs()
    def result() : 
        answer = 0
        for i in graph : 
            for j in i : 
                for k in j : 
                    if k == 0 : 
                        return -1
                    answer = max(answer, k)
        return answer-1
    print(result())