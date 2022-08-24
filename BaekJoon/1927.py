# 백준1927 : 최소 힙
import heapq
import sys
input = sys.stdin.readline
array = []
for _ in range(int(input())) : 
    n = int(input())
    if n==0 : 
        print(heapq.heappop(array) if array else 0)
    else : 
        heapq.heappush(array, n)