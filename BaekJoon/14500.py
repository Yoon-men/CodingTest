# 백준14500 : 테트로미노
import sys; input = sys.stdin.readline

def joyGo(x, y, step, total) : 
    global ans
    if step == 4 : 
        ans = max(ans, total)
        return
    else : 
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]) : 
                if step == 2 :      # 'ㅗ'에 대한 예외 처리
                    visited[nx][ny] = 1
                    joyGo(x, y, step+1, total+Li[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                joyGo(nx, ny, step+1, total+Li[nx][ny])
                visited[nx][ny] = 0


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visited = [[0]*M for _ in range(N)]
    ans = 0
    for i in range(N) : 
        for j in range(M) : 
            visited[i][j] = 1
            joyGo(i, j, 1, Li[i][j])
            visited[i][j] = 0

    print(ans)