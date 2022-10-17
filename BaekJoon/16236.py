# 백준16236 : 아기 상어
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(x, y, s) : 
    dq = deque([(x, y)])
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    candidate = []
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) and (graph[nx][ny] <= s) : 
                dq.append((nx, ny))
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if (graph[nx][ny] < s) and (graph[nx][ny] != 0) : 
                    candidate.append((nx, ny, distance[nx][ny]))
    return sorted(candidate, key=lambda x : (-x[2], -x[0], -x[1]))

if __name__ == "__main__" : 
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for i in range(N) : 
        for j in range(N) : 
            if graph[i][j] == 9 : 
                x, y = i, j
    size = 2

    sizeCnt = 0
    ans = 0
    while True : 
        able = joyGo(x, y, size)
        if not able : 
            break
        nx, ny, distance = able.pop()

        ans += distance
        graph[x][y], graph[nx][ny] = 0, 0
        x, y = nx, ny
        sizeCnt += 1
        if sizeCnt == size : 
            size += 1
            sizeCnt = 0

    print(ans)