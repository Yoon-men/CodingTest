# 백준14567 : 선수과목 (Prerequisite)
import sys ; input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) : 
    A, B = map(int, input().split())
    graph[A].append(B)
ans = [1]*(N+1)
for i in range(1, N+1) : 
    for j in graph[i] : 
        ans[j] = max(ans[j], ans[i]+1)
print(*ans[1:])