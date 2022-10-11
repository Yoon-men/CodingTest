# 백준2015 : 수들의 합 4
import sys ; input = sys.stdin.readline

N, K = map(int, input().split())
Li = list(map(int, input().split()))

prefixLi = [0] * (N+1)
for i in range(1, N+1) : 
    prefixLi[i] = prefixLi[i-1] + Li[i-1]

prefixDi = {}
ans = 0
for i in range(N+1) : 
    ans += prefixDi.get(prefixLi[i]-K, 0)
    prefixDi[prefixLi[i]] = prefixDi.get(prefixLi[i], 0) + 1

print(ans)