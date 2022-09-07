# 백준9461 : 파도반 수열
import sys ; input = sys.stdin.readline
for _ in range(int(input())) : 
    Li = [1,1,1,2]
    N = int(input())
    for i in range(4, N) : 
        Li.append(Li[i-1] + Li[i-2] - Li[i-4])
    print(Li[N-1])