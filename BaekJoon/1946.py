# 백준1946 : 신입 사원
import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    N = int(input())
    rank = [0 for __ in range(N)]
    for i in range(N) : 
        rank[i] = list(map(int, input().split()))
    rank.sort()
    cnt = 1
    maxInterview = rank[0][1]
    for i in range(1, N) : 
        if maxInterview > rank[i][1] : 
            cnt += 1
            maxInterview = rank[i][1]
    print(cnt)