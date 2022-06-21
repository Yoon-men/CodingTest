# 백준10026 : 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def check(y, x) : 
    visited[y][x] = 1
    colorSet = canvas[y][x]

    for i in range(4) : 
        around_y = y + around_y_list[i]
        around_x = x + around_x_list[i]
        if (0 <= around_y < N) and (0 <= around_x < N) : 
            if visited[around_y][around_x] == 0 : 
                if canvas[around_y][around_x] == colorSet : 
                    check(around_y, around_x)


if __name__ == "__main__" : 
    N = int(input())
    canvas = [list(input().strip()) for _ in range(N)]

    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    firstCount, secondCount = 0, 0
    around_y_list = [0, 0, -1, 1]
    around_x_list = [-1, 1, 0, 0]
    
    for i in range(N) : 
        for j in range(N) : 
            if visited[i][j] == 0 : 
                check(i, j)
                firstCount += 1
    
    # Change color (R -> G)
    for i in range(N) : 
        for j in range(N) : 
            if canvas[i][j] == "R" : 
                canvas[i][j] = "G"
    
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) : 
        for j in range(N) : 
            if visited[i][j] == 0 : 
                check(i, j)
                secondCount += 1

    print(firstCount, secondCount)