# 백준2667 : 단지번호붙이기
from collections import deque
import sys ; input = sys.stdin.readline

def joyGo(i, j) : 
    dq = deque([(i, j)])
    global graph
    graph[i][j] = 0
    cnt = 1
    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny]) : 
                graph[nx][ny] = 0
                dq.append((nx, ny))
                cnt += 1
    
    return cnt

if __name__ == "__main__" : 
    N = int(input())
    graph = [list(map(int, input().strip())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    cntLi = []
    for i in range(N) : 
        for j in range(N) : 
            if graph[i][j] : cntLi.append(joyGo(i, j))
    
    print(len(cntLi))
    print("\n".join(str(i) for i in sorted(cntLi)))