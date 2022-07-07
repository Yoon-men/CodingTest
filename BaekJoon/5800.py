# 백준5800 : 성적 통계
import sys
input = sys.stdin.readline

K = int(input())
for i in range(K) : 
    scores = list(map(int, input().split()))
    studentsNum = scores[0]
    del scores[0]

    scores.sort()
    difference = [0] * (studentsNum-1)
    for j in range(studentsNum-1) : 
        difference[j] = scores[j+1] - scores[j]

    print(f"Class {i+1}")
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {max(difference)}")