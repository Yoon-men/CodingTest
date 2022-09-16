# 백준4358 : 생태학
from collections import defaultdict
import sys ; input = sys.stdin.readline
T = defaultdict(int)
n = 0
while True : 
    t = input().strip()
    if not t : break
    else : 
        T[t] += 1
        n += 1
TLi = sorted(list(T.keys()))
for t in TLi : 
    print(f"{t} {T[t]/n*100:.4f}")