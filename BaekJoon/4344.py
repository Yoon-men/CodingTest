# 평균은 넘겠지
import sys
input = sys.stdin.readline
C = int(input())
for _ in range(C) : 
    scores = list(map(int, input().split()))
    average = sum(scores[1:])/scores[0]
    goodBoy = 0
    for i in scores[1:] : 
        if i > average : 
            goodBoy += 1
    percentage = goodBoy/scores[0]*100
    print(f"{percentage:.3f}%")