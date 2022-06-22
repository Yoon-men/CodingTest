# 백준20949 : 효정과 새 모니터
from math import sqrt
import sys
input = sys.stdin.readline

N = int(input())
monitors = []

for i in range(N) : 
    W, H = map(int, input().split())
    monitors.append([i+1, sqrt(W**2 + H**2) / 77])

for i in sorted(monitors, key=lambda x : (-x[1], x[0])) : 
    print(i[0])