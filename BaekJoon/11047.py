# 백준11047 : 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
price = [0] * N
for i in range(N) : 
    price[i] = int(input())

cnt = 0
for i in sorted(price, reverse=True) : 
    cnt += K//i
    K %= i

print(cnt)