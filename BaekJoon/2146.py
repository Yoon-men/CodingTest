# 백준2146 : 다리 만들기
import sys; input = sys.stdin.readline
from collections import deque

def islandClassification(i, j) : 
    dq = deque([(i, j)])
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny]) and (not visited[nx][ny]) : 
                visited[nx][ny] = 1
                graph[nx][ny] = islandNum
                dq.append((nx, ny))


def shortestDistanceFinding(islandNumber) : 
    dq = deque()
    distLi = [[-1]*N for _ in range(N)]

    for i in range(N) : 
        for j in range(N) : 
            if graph[i][j] == islandNumber : 
                distLi[i][j] = 0
                dq.append((i, j))

    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) : 
                if (graph[nx][ny]) and (graph[nx][ny] != islandNumber) : 
                    return distLi[x][y]
                elif (not graph[nx][ny]) and (distLi[nx][ny] == -1) : 
                    distLi[nx][ny] = distLi[x][y] + 1
                    dq.append((nx, ny))


if __name__ == "__main__" : 
    # Input data
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # Classify island
    visited = [[0]*N for _ in range(N)]
    islandNum = 1
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range(N) : 
        for j in range(N) : 
            if (graph[i][j]) and (not visited[i][j]) : 
                visited[i][j] = 1
                graph[i][j] = islandNum
                islandClassification(i, j)
                islandNum += 1

    # Find shortest distance
    distance = sys.maxsize
    for i in range(1, islandNum) : 
        distance = min(distance, shortestDistanceFinding(i))

    # Print answer
    print(distance)