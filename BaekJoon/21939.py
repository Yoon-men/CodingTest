# 백준21939 : 문제 추천 시스템 Version 1
import heapq
import sys ; input = sys.stdin.readline

mx, mn = [], []
PLi = {}
for _ in range(int(input())) : 
    P, L = map(int, input().split())
    heapq.heappush(mx, (-L, -P))
    heapq.heappush(mn, (L, P))
    PLi[P] = L

for _ in range(int(input())) : 
    cmd = input().split()
    P = int(cmd[1])
    if cmd[0]=="add" : 
        L = int(cmd[2])
        heapq.heappush(mx, (-L, -P))
        heapq.heappush(mn, (L, P))
        PLi[P] = L
    elif cmd[0]=="solved" : 
        PLi[P] = 0
    else : 
        if P==1 : 
            while mx and PLi[-mx[0][1]] != -mx[0][0] : heapq.heappop(mx)
            print(-mx[0][1])
        else : 
            while mn and PLi[mn[0][1]] != mn[0][0] : heapq.heappop(mn)
            print(mn[0][1])