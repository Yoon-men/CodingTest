# 백준25600 : Triathlon
import sys ; input = sys.stdin.readline
score = []
for _ in range(int(input())) : 
    a, d, g = map(int, input().split())
    if a==d+g : score.append(a*(d+g)*2) 
    else : score.append(a*(d+g))
print(max(score))