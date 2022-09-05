# 백준2630 : 색종이 만들기
import sys ; input = sys.stdin.readline

def joyGo(x, y, n) : 
    global white, blue
    c = Li[x][y]
    for i in range(x, x+n) : 
        for j in range(y, y+n) : 
            if c != Li[i][j] : 
                joyGo(x, y, n//2) # 1
                joyGo(x, y+n//2, n//2) # 2
                joyGo(x+n//2, y, n//2) # 3
                joyGo(x+n//2, y+n//2, n//2) # 4
                return
    if c==0 : white += 1
    else : blue += 1

if __name__ == "__main__" : 
    N = int(input())
    Li = [list(map(int, input().split())) for _ in range(N)]
    white = 0 ; blue = 0
    joyGo(0, 0, N)
    print(f"{white}\n{blue}")