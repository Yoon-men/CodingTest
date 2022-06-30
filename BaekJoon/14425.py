# 백준14425 : 문자열 집합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input() for _ in range(N)])

answer = 0
for _ in range(M):
    T = input()
    if T in S:
        answer += 1
print(answer)