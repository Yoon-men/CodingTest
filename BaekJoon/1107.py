# 백준1107 : 리모컨
import sys ; input = sys.stdin.readline
N = int(input())
M = int(input())
bt = list(map(int, input().split()))
cnt = abs(100-N)
for i in range(1000001) : 
    for j in range(len(str(i))) : 
        if int(str(i)[j]) in bt : break
        elif (j==len(str(i))-1) : cnt = min(cnt, len(str(i))+abs(i-N))
print(cnt)