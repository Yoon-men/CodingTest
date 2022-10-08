# 백준1043 : 거짓말
import sys ; input = sys.stdin.readline

N, M = map(int, input().split())
trueJoyGo = set(input().split()[1:])

party = [[] for _ in range(M)]
for i in range(M) : 
    party[i] = set(input().split()[1:])

for _ in range(M) : 
    for i in party : 
        if trueJoyGo & i : trueJoyGo = trueJoyGo | i
ans = 0
for i in party : 
    if not trueJoyGo & i : ans += 1
print(ans)