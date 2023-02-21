# 백준17608 : 막대기
import sys; input = sys.stdin.readline
Li = [int(input()) for _ in range(int(input()))]
M = Li[-1]
ans = 1
for i in Li[::-1] : 
    if i > M : ans += 1; M = i
print(ans)