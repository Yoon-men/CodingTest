# 백준11497 : 통나무 건너뛰기
import sys
input = sys.stdin.readline
for _ in range(int(input())) : 
    N = int(input())
    logs = list(map(int, input().split()))
    maxDif = 0
    logs.sort(reverse=True)
    for i in range(N-2) : 
        maxDif = max(maxDif, logs[i] - logs[i+2])
    print(maxDif)