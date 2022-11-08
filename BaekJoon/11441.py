# 백준11441 : 합 구하기
import sys ; input = sys.stdin.readline
N = int(input())
Li = list(map(int, input().split()))

prefixLi = [0] * (N+1)
for i in range(1, N+1) : 
    prefixLi[i] = prefixLi[i-1] + Li[i-1]

for _ in range(int(input())) : 
    i, j = map(int, input().split())
    print(prefixLi[j] - prefixLi[i-1])