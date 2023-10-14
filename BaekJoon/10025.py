# 백준10025 : 게으른 백곰
import sys; input = sys.stdin.readline

N, K = map(int, input().split())
cage = [0] * (10**6 + 1)
for i in range(N):
    g, x = map(int, input().split())
    cage[x] = g

range_ = 2*K + 1
sum_checker = ans = sum(cage[:range_])
for i in range(range_, 10**6 + 1):
    sum_checker += (cage[i] - cage[i-range_])
    ans = max(ans, sum_checker)

print(ans)