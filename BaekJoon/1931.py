# 백준1931 : 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
order = [[0]*2 for _ in range(N)]
for i in range(N) : 
    order[i][0], order[i][1] = map(int, input().split())
order.sort(key=lambda x : (x[1], x[0]))

e = order[0][1]
cnt = 1
for i in range(1, N) : 
    if order[i][0] >= e : 
        cnt += 1
        e = order[i][1]

print(cnt)