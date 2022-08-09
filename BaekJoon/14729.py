# 백준14729 : 칠무해
import sys
input = sys.stdin.readline
scr = [float(input()) for _ in range(int(input()))]
for i in sorted(scr)[:7] : 
    print(f"{i:.3f}")