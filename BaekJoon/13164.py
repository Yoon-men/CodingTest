# 백준13164 : 행복 유치원
N, K = map(int, input().split())
H = list(map(int, input().split()))
Li = sorted([H[i] - H[i-1] for i in range(1, N)], reverse=True)
print(sum(Li[K-1:]))