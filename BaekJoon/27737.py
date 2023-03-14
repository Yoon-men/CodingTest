# 백준27737 : 버섯 농장
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(x: int, y: int) -> int : 
    dq = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1

    while dq : 
        x, y = dq.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) and (not graph[nx][ny]) : 
                dq.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


def check(cntLi: list, _range: int, sporeNum: int) -> None : 
    if not cntLi : 
        print("IMPOSSIBLE")
        return
    spore = 0
    for cnt in cntLi : 
        spore += cnt//_range
        if cnt%_range > 0 : spore += 1
    if sporeNum >= spore : 
        print("POSSIBLE")
        print(sporeNum - spore)
    else : 
        print("IMPOSSIBLE")


if __name__ == "__main__" : 
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[0]*N for _ in range(N)]
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    Li = []
    for i in range(N) : 
        for j in range(N) : 
            if not graph[i][j] and not visited[i][j] : 
                Li.append(joyGo(i, j))

    check(cntLi=Li, _range=K, sporeNum=M)