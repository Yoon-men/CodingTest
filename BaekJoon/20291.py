# 백준20291 : 파일 정리
from collections import defaultdict
import sys ; input = sys.stdin.readline
di = defaultdict(int)
for _ in range(int(input())) : 
    exts = input().split(".")[1]
    di[exts.strip()] += 1
for i in sorted(di) : 
    print(i, di[i])