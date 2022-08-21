# 백준11279 : 최대 힙
import heapq
import sys
input = sys.stdin.readline
array = []
for _ in range(int(input())) : 
    n = int(input())
    if n == 0 : 
        if array : 
            print(abs(heapq.heappop(array)))
        else : 
            print(0)
    else : 
        heapq.heappush(array, -n)