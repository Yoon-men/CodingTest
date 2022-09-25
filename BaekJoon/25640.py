# 백준25640 : MBTI
import sys ; input = sys.stdin.readline
m = input().strip()
answer = 0
for _ in range(int(input())) : 
    if m==input().strip() : answer += 1
print(answer)