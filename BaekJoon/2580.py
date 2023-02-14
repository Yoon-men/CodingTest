# 백준2580 : 스도쿠
import sys; input = sys.stdin.readline

def chk(x, y) : 
    # 가로, 세로로 숫자 맞아떨어지는지 체크
    Li = [i for i in range(1, 10)]
    for i in range(9) : 
        xNum, yNum = graph[x][i], graph[i][y]
        if xNum in Li : Li.remove(xNum)
        if yNum in Li : Li.remove(yNum)

    # 3×3으로 숫자 맞아떨어지는지 체크
    nx, ny = x//3*3, y//3*3
    for i in range(3) : 
        for j in range(3) : 
            num = graph[nx+i][ny+j]
            if num in Li : Li.remove(num)

    return Li


def DFS(n) : 
    if n == len(BLitzcrANK) : 
        for line in range(9) : 
            print(*graph[line])
        sys.exit()
    
    i, j = BLitzcrANK[n]
    for num in chk(i, j) : 
        graph[i][j] = num
        DFS(n+1)
        graph[i][j] = 0


if __name__ == "__main__" : 
    graph = [list(map(int, input().split())) for _ in range(9)]
    # graph = [list(map(int, "0 3 5 4 6 9 2 7 8".split())), list(map(int, "7 8 2 1 0 5 6 0 9".split())), list(map(int, "0 6 0 2 7 8 1 3 5".split())), list(map(int, "3 2 1 0 4 6 8 9 7".split())), list(map(int, "8 0 4 9 1 3 5 0 6".split())), list(map(int, "5 9 6 8 2 0 4 1 3".split())), list(map(int, "9 1 7 6 5 2 0 8 0".split())), list(map(int, "6 0 3 7 0 1 9 5 2".split())), list(map(int, "2 5 8 3 9 4 7 6 0".split()))]               # Test code / please delete the contents of this line.
    BLitzcrANK = [(i, j) for i in range(9) for j in range(9) if not graph[i][j]]
    
    DFS(0)