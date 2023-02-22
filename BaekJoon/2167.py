# 백준2167 : 2차원 배열의 합
import sys; input = sys.stdin.readline

def makePrefixSumList(height, width, Li) : 
    prefixSumLi = [[0]*(width+1) for _ in range(height+1)]
    for i in range(1, height+1) : 
        for j in range(1, width+1) : 
            prefixSumLi[i][j] = prefixSumLi[i][j-1] + prefixSumLi[i-1][j] - prefixSumLi[i-1][j-1] + Li[i-1][j-1]

    return prefixSumLi


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = [list(map(int, input().split())) for _ in range(N)]

    prefixSumLi = makePrefixSumList(N, M, Li)

    for _ in range(int(input())) : 
        i, j, x, y = map(int, input().split())
        print(prefixSumLi[x][y] - prefixSumLi[i-1][y] - prefixSumLi[x][j-1] + prefixSumLi[i-1][j-1])