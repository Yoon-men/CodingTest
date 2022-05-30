# 백준1764 : 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notListen = [input().strip() for _ in range(N)]
notSee = [input().strip() for _ in range(M)]

notListenANDSee = list(set(notListen) & set(notSee))

print(len(notListenANDSee))
for name in sorted(notListenANDSee) : 
    print(name)