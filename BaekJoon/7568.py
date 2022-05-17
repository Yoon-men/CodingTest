# 덩치
import sys
input = sys.stdin.readline
N = int(input())
man = []

for _ in range(N) : 
    weight, height = map(int, input().split())
    man.append((weight, height))

for i in man : 
    ranking = 1
    for j in man : 
        if i[0] < j[0] and i[1] < j[1] : 
            ranking += 1
    print(ranking, end=" ")