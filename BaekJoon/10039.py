# 평균 점수
import sys
score = [0] * 5
for i in range(5) : 
    score[i] = int(sys.stdin.readline())
    if score[i] < 40 : 
        score[i] = 40
print(sum(score)//5)