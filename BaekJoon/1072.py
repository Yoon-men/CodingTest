# 백준1072 : 게임
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X
if Z >= 99 : 
    print(-1)
else : 
    answer = 0
    start, end = 1, X
    while start <= end : 
        mid = (start+end) // 2
        if (Y+mid)*100//(X+mid) <= Z : 
            start = mid + 1
        else : 
            answer = mid
            end = mid - 1
    print(answer)