# 백준1405 : 미친 로봇
import sys ; input = sys.stdin.readline

def joyGo(x, y, record, tmp) : 
    global ans
    if len(record) == T+1 : 
        ans += tmp
        return
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in record : 
            record.append((nx, ny))
            joyGo(nx, ny, record, tmp*P[i])
            record.pop()

if __name__ == "__main__" : 
    T, E, W, S, N = map(int, input().split())
    P = [E, W, S, N]

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    ans = 0
    joyGo(0, 0, [(0, 0)], 1)
    
    print(ans * 0.01**T)