# 백준1011 : Fly me to the Alpha Centauri
import sys ; input = sys.stdin.readline

for _ in range(int(input())) : 
    x, y = map(int, input().split())
    dist = y - x
    n = 0
    while dist > n*(n+1) : 
        n += 1
    print(n*2 - 1 if dist <= n**2 else n*2)