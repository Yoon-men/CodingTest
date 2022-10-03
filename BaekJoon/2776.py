# 백준2776 : 암기왕
import sys ; input = sys.stdin.readline
for _ in range(int(input())) : 
    N = int(input())
    Li_1 = set(map(int, input().split()))
    M = int(input())
    Li_2 = list(map(int, input().split()))
    for i in Li_2 : 
        print(1 if i in Li_1 else 0)