# 백준21736 : 헌내기는 친구가 필요해
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(N: int, M: int, maps: list) -> str : 
    def DFS(x, y) : 
        global ans
        visited[x][y] = 1
        if maps[x][y] == 'P' : ans += 1
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]) : 
                if maps[nx][ny] == 'X' : continue
                DFS(nx, ny)

            
    
    global ans
    ans = 0
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    
    for i in range(N) : 
        for j in range(M) : 
            if maps[i][j] == 'I' : 
                DFS(i, j)
    
    return ans if ans > 0 else "TT"
    



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    maps = [list(input().strip()) for _ in range(N)]

    print(joyGo(N, M, maps))