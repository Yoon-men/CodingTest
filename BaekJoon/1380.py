# 백준1380 : 귀걸이
import sys ; input = sys.stdin.readline

scenario = 1
while True : 
    N = int(input())
    if not N : break

    nameLi = [input().strip() for _ in range(N)]
    Li = [0] * N
    for _ in range(2*N - 1) : 
        idx, _ = input().split()
        Li[int(idx) - 1] += 1       # 1 = 압수당함 / 2 = 돌려받음
    
    for i in range(N) : 
        if Li[i] != 2 : 
            ans = nameLi[i]
            break
    
    print(f"{scenario} {ans}")
    scenario += 1