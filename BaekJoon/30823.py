# 백준30823 : 건공문자열
import sys; input = sys.stdin.readline

N, K = map(int, input().split())
S = list(input().strip())

print(''.join(S[K-1:] + (S[:K-1])[::-1 if (N-K-1) % 2 else 1]))