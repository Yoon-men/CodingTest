# 백준21608 : 상어 초등학교
import sys ; input = sys.stdin.readline

N = int(input())
seatLi = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0 

wantDi = {}
for _ in range(N**2) : 
    Li = list(map(int, input().split()))
    wantDi[Li[0]] = Li[1:]

    mx_x = 0
    mx_y = 0
    mx_want = -1
    mx_empty = -1
    for i in range(N) : 
        for j in range(N) : 
            if not seatLi[i][j] : 
                wantCnt = 0
                emptyCnt = 0
                for k in range(4) : 
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (0 <= nx < N) and (0 <= ny < N) : 
                        if seatLi[nx][ny] in wantDi[Li[0]] : wantCnt += 1
                        if not seatLi[nx][ny] : emptyCnt += 1
                
                if (mx_want < wantCnt) or (mx_want == wantCnt and mx_empty < emptyCnt) : 
                    mx_x = i
                    mx_y = j
                    mx_want = wantCnt
                    mx_empty = emptyCnt

    seatLi[mx_x][mx_y] = Li[0]

for i in range(N) : 
    for j in range(N) : 
        cnt = 0
        wantLi = wantDi[seatLi[i][j]]
        for k in range(4) : 
            nx = i + dx[k]
            ny = j + dy[k]
            if (0 <= nx < N) and (0 <= ny < N) : 
                if seatLi[nx][ny] in wantLi : cnt += 1
        if cnt > 0 : 
            ans += 10**(cnt-1)

print(ans)