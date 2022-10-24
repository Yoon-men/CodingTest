# 백준1780 : 종이의 개수
import sys ; input = sys.stdin.readline

def joyGo(x, y, n) : 
    chk = graph[x][y]
    for i in range(x, x+n) : 
        for j in range(y, y+n) : 
            if graph[i][j] != chk : 
                for k in range(3) : 
                    for l in range(3) : 
                        joyGo(x + k*n//3, y + l*n//3, n//3)
                return
    global ans
    if chk == -1 : ans[0] += 1
    elif chk == 0 : ans[1] += 1
    else : ans[2] += 1

if __name__ == "__main__" : 
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = [0, 0, 0]
    joyGo(0, 0, N)
    print("\n".join(str(i) for i in ans))