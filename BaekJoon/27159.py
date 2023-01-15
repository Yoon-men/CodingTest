# 백준27159 : 노 땡스!
import sys; input = sys.stdin.readline

_ = int(input())
Li = list(map(int, input().split()))

ans = []
before = -1
for i in Li : 
    if i != before+1 : ans.append(i)
    before = i

print(sum(ans))