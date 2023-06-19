# 백준5054 : 주차의 신
import sys; input = sys.stdin.readline

for _ in range(int(input())) : 
    __ = int(input())
    Li = sorted(list(map(int, input().split())))
    print((Li[-1]-Li[0]) * 2)