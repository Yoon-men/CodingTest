# 백준26150 : Identify, Sort, Index, Solve
import sys ; input = sys.stdin.readline

N = int(input())
Li = [0] * N
for i in range(N) : 
    t, n, d = input().split()
    Li[i] = [t, int(n), int(d)]

ans = [0] * N
Li.sort(key=lambda x : x[1])
for i in range(N) : 
    ans[i] = Li[i][0][Li[i][2]-1].upper()

print("".join(ans))