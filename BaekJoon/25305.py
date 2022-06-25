# 백준25305 : 커트라인
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
scores = sorted(list(map(int, input().split())))

print(scores[-k])