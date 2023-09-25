# 백준16493 : 최대 페이지 수
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, M: int, schedule_list: List[Tuple[int, int]]) : 
    dp = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1, M+1) : 
        weight, value = schedule_list[i-1]
        for j in range(1, N+1) : 
            if j < weight : dp[i][j] = dp[i-1][j]
            else : dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    
    return dp[M][N]


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    schedule_list = [tuple(map(int, input().split())) for _ in range(M)]

    print(joyGo(N, M, schedule_list))