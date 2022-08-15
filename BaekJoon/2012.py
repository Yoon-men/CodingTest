# 백준2012 : 등수 매기기
import sys
input = sys.stdin.readline
rank = []
N = int(input())
for _ in range(N) : 
    rank.append(int(input()))
rank.sort()
answer = 0
for i in range(N) : 
    answer += abs(rank[i] - (i+1))
print(answer)