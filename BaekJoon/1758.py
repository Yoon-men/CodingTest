# 백준1758 : 알바생 강호
import sys
input = sys.stdin.readline
N = int(input())
tips = [int(input()) for _ in range(N)]
answer = 0
tips.sort(reverse=True)
for i in range(N) : 
    tip = tips[i] - i
    if tip > 0 : 
        answer += tip
print(answer)