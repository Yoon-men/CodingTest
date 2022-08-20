# 백준2109 : 순회강연
import heapq
import sys
input = sys.stdin.readline
request = []
for _ in range(int(input())) : 
    pay, day = map(int, input().split())
    request.append([pay, day])
request.sort(key=lambda q : q[1])
answer = []
for i in request : 
    heapq.heappush(answer, i[0])
    if len(answer) > i[1] : 
        heapq.heappop(answer)
print(sum(answer))