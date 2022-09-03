# 백준1697 : 숨바꼭질
from collections import deque
N, K = map(int, input().split())
mx = 10**5
times = [0] * (mx+1)
q = deque([N])
while q : 
    L = q.popleft()
    if L==K : print(times[L]) ; break
    for x in (L-1, L+1, L*2) : 
        if 0 <= x <= mx and not times[x] : 
            times[x] = times[L] + 1
            q.append(x)