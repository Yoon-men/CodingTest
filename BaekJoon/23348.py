# 백준23348 : 스트릿 코딩 파이터
import sys
input = sys.stdin.readline

criteria = list(map(int, input().split()))
N = int(input())

scores = [0] * N
for i in range(N) : 
    for j in range(3) : 
        score = list(map(int, input().split()))
        for k in range(3) : 
            scores[i] += score[k] * criteria[k]

print(max(scores))