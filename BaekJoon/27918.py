# 백준27918 : 탁구 경기
from collections import defaultdict
Di = defaultdict(int)
for _ in range(int(input())): 
    Di[input()] += 1
    if abs(Di['D'] - Di['P']) == 2: break

print(f"{Di['D']}:{Di['P']}")