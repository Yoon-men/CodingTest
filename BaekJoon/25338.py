# 백준25338 : 바지 구매
import sys
input = sys.stdin.readline

answer = 0
a, b, c, d = map(int, input().split())

N = int(input())
for _ in range(N) : 
    C, L = map(int, input().split())
    if C == max(a*(L-b)**2+c, d) : 
        answer += 1

print(answer)