# 백준2075 : N번째 큰 수
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
que = []
for _ in range(N) : 
    Li = list(map(int, input().split()))
    for num in Li : 
        if len(que) < N : heappush(que, num)
        else : 
            if que[0] < num : 
                heappop(que)
                heappush(que, num)

print(que[0])