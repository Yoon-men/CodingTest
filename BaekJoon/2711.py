# 백준2711 : 오타맨 고창영
import sys; input = sys.stdin.readline
for _ in range(int(input())) : 
    N, S = input().split(); N = int(N)
    print(f"{S[:N-1]}{S[N:]}")