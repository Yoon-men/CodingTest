# 백준1374 : 강의실
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
Li = [list(map(int, input().split())) for _ in range(N)]
Li.sort(key=lambda x : x[1])

hq = []
cnt = 0

for i in Li : 
    while (hq) and (hq[0] <= i[1]) : 
        heappop(hq)
    heappush(hq, i[2])
    cnt = max(cnt, len(hq))

print(cnt)