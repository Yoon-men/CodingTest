# 백준1013 : Contact
import sys ; input = sys.stdin.readline
import re

for _ in range(int(input())) : 
    s = input().strip()
    pat = re.compile("(100+1+|01)+")
    print("YES" if pat.fullmatch(s) else "NO")