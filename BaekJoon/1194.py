# 백준1194 : 달이 차오른다, 가자.
from collections import deque
import sys ; input = sys.stdin.readline

def findMe() : 
    global dq, visited
    for i in range(N) : 
        for j in range(M) : 
            if maze[i][j] == "0" :             # 현재 위치
                maze[i][j] = "."
                dq.append([i,j,0,0])
                visited[i][j][0] = 1
                return

def joyGo() : 
    while dq : 
        if dq : x, y, k, cnt = dq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (maze[nx][ny] != "#") and (not visited[nx][ny][k]) : 
                if maze[nx][ny] == "." :        # 빈 칸
                    visited[nx][ny][k] = 1
                    dq.append([nx,ny,k,cnt+1])
                elif maze[nx][ny] == "1" :      # 출구
                    return cnt+1
                else :                          # 열쇠 or 문
                    if maze[nx][ny].isupper() : 
                        if k & 1<<(ord(maze[nx][ny])-65) :          # ord("A") = 65
                            visited[nx][ny][k] = 1
                            dq.append([nx,ny,k,cnt+1])
                    elif maze[nx][ny].islower() : 
                        nk = k | 1<<(ord(maze[nx][ny])-97)          # ord("a") = 97
                        if not visited[nx][ny][nk] : 
                            visited[nx][ny][nk] = 1
                            dq.append([nx,ny,nk,cnt+1])
    return -1


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    maze = [list(input().strip()) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    dq = deque()
    visited = [[[0]*64 for _ in range(M)] for _ in range(N)]

    findMe()
    print(joyGo())