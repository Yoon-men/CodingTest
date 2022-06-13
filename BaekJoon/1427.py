# 백준1427 : 소트인사이드
import sys
N = list(map(int, sys.stdin.readline().strip()))
for i in sorted(N, reverse=True) : 
    print(i, end="")