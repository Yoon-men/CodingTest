# 백준17626 : Four Squares
import sys
N = int(input())
dp = [0] * (N+1) ; dp[1] = 1
for i in range(2, N+1) : 
    mmin = sys.maxsize
    for j in range(1, int(i**0.5) + 1) : 
        mmin = min(mmin, dp[i - j**2])
    dp[i] = mmin + 1
print(dp[N])