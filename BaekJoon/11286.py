# 백준11286 : 절댓값 힙
import heapq
import sys
input = sys.stdin.readline
array = []
for _ in range(int(input())) : 
    n = int(input())
    if n==0 : print(heapq.heappop(array)[1] if array else 0)
    else : heapq.heappush(array, (abs(n), n))