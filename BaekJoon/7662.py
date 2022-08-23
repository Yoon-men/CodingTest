# 백준7662 : 이중 우선순위 큐
import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())) : 
    k = int(input())
    mx, mn = [], []
    joyGo = [0] * k
    for i in range(k) : 
        cmd = input().split()
        n = int(cmd[1])
        if cmd[0] == "I" : 
            heapq.heappush(mx, (-n, i))
            heapq.heappush(mn, (n, i))
            joyGo[i] = 1
        else : 
            if n==1 : 
                while mx and not joyGo[mx[0][1]] : heapq.heappop(mx)
                if mx : joyGo[mx[0][1]] = 0 ; heapq.heappop(mx)
            else : 
                while mn and not joyGo[mn[0][1]] : heapq.heappop(mn)
                if mn : joyGo[mn[0][1]] = 0 ; heapq.heappop(mn)
    while mx and not joyGo[mx[0][1]] : heapq.heappop(mx)
    while mn and not joyGo[mn[0][1]] : heapq.heappop(mn)
    print("EMPTY" if not mx or not mn else f"{-mx[0][0]} {mn[0][0]}")