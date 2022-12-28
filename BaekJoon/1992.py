# 백준1992 : 쿼드트리
import sys; input = sys.stdin.readline

def joyGo(x, y, n) : 
    target = Li[x][y]
    for i in range(x, x+n) : 
        for j in range(y, y+n) : 
            if target != Li[i][j] : 
                target = -1
                break

    if target == -1 : 
        print("(", end="")
        joyGo(x, y, n//2)    # 1
        joyGo(x, y+n//2, n//2)    # 2
        joyGo(x+n//2, y, n//2)    # 3
        joyGo(x+n//2, y+n//2, n//2)    # 4
        print(")", end="")
    elif target == 1 : 
        print(1, end="")
    elif target == 0 : 
        print(0, end="")


if __name__ == "__main__" : 
    N = int(input())
    Li = [list(map(int, input().strip())) for _ in range(N)]
    joyGo(0, 0, N)