# 백준4963 : 섬의 개수
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(w: int, h: int, _map: list) -> int : 
    def DFS(x: int, y: int) : 
        _map[x][y] = 2

        for i in range(8) :  
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < h) and (0 <= ny < w) and (_map[nx][ny] == 1) : 
                DFS(nx, ny)

    ans = 0

    dx, dy = [-1,0,1,1,1,0,-1,-1], [1,1,1,0,-1,-1,-1,0]
    for i in range(h) : 
        for j in range(w) : 
            if _map[i][j] == 1 : 
                DFS(i, j)
                ans += 1
    
    return ans


if __name__ == "__main__" : 
    while True : 
        w, h = map(int, input().split())
        if (w == 0) and (h == 0) : break

        _map = [list(map(int, input().split())) for _ in range(h)]
        print(joyGo(w, h, _map))