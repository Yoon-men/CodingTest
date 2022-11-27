# 백준26068 : 치킨댄스를 추는 곰곰이를 본 임스 2
import sys ; input = sys.stdin.readline
N = int(input())
Li = [int(input().split("-")[1]) for _ in range(N)]
ans = 0
for i in Li : 
    if i <= 90 : ans += 1
print(ans)