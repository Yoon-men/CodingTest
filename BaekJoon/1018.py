# 백준1018 : 체스판 다시 칠하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

revise = []
for i in range(N - 7) : 
    for j in range(M - 7) : 
        W, B = 0, 0
        for k in range(i, i+8) : 
            for l in range(j, j+8) : 
                if (k+l) % 2 == 0 : 
                    if board[k][l] != "W" : 
                        W += 1
                    if board[k][l] != "B" : 
                        B += 1
                else : 
                    if board[k][l] != "W" : 
                        B += 1
                    if board[k][l] != "B" : 
                        W += 1
        revise.append(W)
        revise.append(B)

print(min(revise))