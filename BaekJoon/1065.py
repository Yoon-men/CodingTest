# 백준1065 : 한수
import sys
N = int(sys.stdin.readline())
num = 0

for i in range(1, N+1) : 
    NLi = list(map(int, str(i)))
    if i < 100 : 
        num += 1
    elif NLi[0]-NLi[1] == NLi[1]-NLi[2] : 
        num += 1

print(num)