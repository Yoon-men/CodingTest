# 좌표 정렬하기
import sys
input = sys.stdin.readline
N = int(input())
dots = []
for _ in range(N) : 
    x, y = map(int, input().split())
    dots.append((x, y))
dots.sort()
for i in dots : 
    print(f"{i[0]} {i[1]}")