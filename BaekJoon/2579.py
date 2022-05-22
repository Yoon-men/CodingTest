# 계단 오르기
import sys
input = sys.stdin.readline
N = int(input())
stairs = []
GEToDAZE = []
for _ in range(N) : 
    stairs.append(int(input()))

if N == 1 : 
    print(stairs[0])
elif N == 2 : 
    print(stairs[0] + stairs[1])
else : 
    GEToDAZE.append(stairs[0])
    GEToDAZE.append(stairs[0] + stairs[1])
    GEToDAZE.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
    for i in range(3, N) : 
        GEToDAZE.append(max(GEToDAZE[i - 3] + stairs[i - 1] + stairs[i], GEToDAZE[i - 2] + stairs[i]))
    print(GEToDAZE[-1])