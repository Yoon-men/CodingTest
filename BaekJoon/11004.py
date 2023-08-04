# 백준11004 : K번째 수
N, K = map(int, input().split())
print(sorted(list(map(int, input().split())))[K-1])