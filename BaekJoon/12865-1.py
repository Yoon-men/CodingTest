# 백준12865 : 평범한 배낭
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, K: int, stuffs: List[Tuple[int, int]]) : 
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1) : 
        weight, value = stuffs[i-1]
        for j in range(1, K+1) : 
            if j < weight : dp[i][j] = dp[i-1][j]
            else : dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    return dp[N][K]


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    stuffs = [tuple(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, K, stuffs))