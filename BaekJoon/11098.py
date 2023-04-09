# 백준 11098 : 첼시를 도와줘!
import sys; input = sys.stdin.readline

for _ in range(int(input())) : 
    Di = {}
    for __ in range(int(input())) : 
        cost, name = input().split(); cost = int(cost)
        Di[cost] = name
    print(sorted(Di.items())[-1][1])