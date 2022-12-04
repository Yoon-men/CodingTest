# 백준26145 : 출제비 재분배
import sys ; input = sys.stdin.readline

N, M = map(int, input().split())
examinerLi = list(map(int, input().split()))

ansLi = [0] * (N+M)
for i in range(N) : 
    distributionLi = list(map(int, input().split()))
    for j in range(N+M) : 
        ansLi[j] += distributionLi[j]
        examinerLi[i] -= distributionLi[j]

for i in range(N) : 
    ansLi[i] += examinerLi[i]

print(*ansLi)