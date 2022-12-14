# 백준1337 : 올바른 배열
import sys ; input = sys.stdin.readline
Li = sorted([int(input()) for _ in range(int(input()))])
cntLi = []
for i in range(len(Li)) : 
    cnt = 0
    for j in range(Li[i], Li[i]+5) : 
        if j not in Li : cnt += 1
    cntLi.append(cnt)
print(min(cntLi))