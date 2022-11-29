# 백준2822 : 점수 계산
import sys ; input = sys.stdin.readline
Li = [int(input()) for _ in range(8)]
score = 0
idx = []
for i in sorted(Li, reverse=True)[0:5] : 
    score += i
    idx.append(Li.index(i)+1)
print(score)
print(*sorted(idx))