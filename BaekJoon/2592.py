# 백준2592 : 대표값
import sys; input = sys.stdin.readline
from collections import defaultdict
Li = [int(input()) for _ in range(10)]
print(sum(Li) // 10)
Di = defaultdict(int)
for i in Li : 
    Di[i] += 1
Di = Di.items()
ans = max(Di, key=lambda x : x[1])
print(ans[0])