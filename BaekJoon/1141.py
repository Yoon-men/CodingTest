# 백준1141 : 접두사
import sys ; input = sys.stdin.readline

N = int(input())
Li = sorted([input().strip() for _ in range(N)], key=len)

ans = 0
for i in range(N) : 
    chk = 0
    for j in range(i+1, N) : 
        if Li[i] == Li[j][0:len(Li[i])] : chk = 1 ; break
    if not chk : ans += 1

print(ans)