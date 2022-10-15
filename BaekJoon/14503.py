# 백준14503 : 로봇 청소기
import sys ; input = sys.stdin.readline

def backCheck() : 
    global x, y
    if direction == 0 : 
        if mapLi[x+1][y] : return 1
        else : x += 1
    elif direction == 1 : 
        if mapLi[x][y-1] : return 1
        else : y -= 1
    elif direction == 2 : 
        if mapLi[x-1][y] : return 1
        else : x -= 1
    elif direction == 3 : 
        if mapLi[x][y+1] : return 1
        else : y += 1
    return 0

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    x, y, direction = map(int, input().split())
    mapLi = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    ans = 1
    while True : 
        cleaning = 0
        for _ in range(4) : 
            direction = (direction+3) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            if (0 <= nx < N) and (0 <= ny < M) and (not mapLi[nx][ny]) and (not visited[nx][ny]) : 
                visited[nx][ny] = 1
                ans += 1
                x = nx ; y = ny
                cleaning = 1
                break
        if not cleaning : 
            if backCheck() : break

    print(ans)