# 백준9095 : 1, 2, 3 더하기
import sys ; input = sys.stdin.readline
for _ in range(int(input())) : 
    n = int(input())
    Li = [1, 2, 4]
    for i in range(3, n+1) : 
        Li.append(Li[i-3]+Li[i-2]+Li[i-1])
    print(Li[n-1])