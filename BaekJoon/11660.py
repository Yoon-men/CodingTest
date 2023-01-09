# 백준11660 : 구간 합 구하기 5
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
Li = [list(map(int, input().split())) for _ in range(N)]

sumLi = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1) : 
    for j in range(1, N+1) : 
        sumLi[i][j] = sumLi[i][j-1] + sumLi[i-1][j] - sumLi[i-1][j-1] + Li[i-1][j-1]

for _ in range(M) : 
    x1, y1, x2, y2 = map(int, input().split())
    print(sumLi[x2][y2] - sumLi[x1-1][y2] - sumLi[x2][y1-1] + sumLi[x1-1][y1-1])