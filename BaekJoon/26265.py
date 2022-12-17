# 백준26265 : 멘토와 멘티
import sys ; input = sys.stdin.readline
from collections import defaultdict

N = int(input())
Di = defaultdict(list)
for i in range(N) : 
    a, b = input().split()
    Di[a].append(b)
Li = sorted(Di.items())
for i in Li : 
    for j in sorted(i[1], reverse=True) : 
        print(i[0], j)