# 백준14728 : 벼락치기
import sys ; input = sys.stdin.readline

def chk(T, tLi, sLi, N) : 
    dp = [[0]*(T+1) for _ in range(N+1)]
    for i in range(1, N+1) : 
        for j in range(1, T+1) : 
            if tLi[i-1] <= j : 
                dp[i][j] = max(sLi[i-1] + dp[i-1][j-tLi[i-1]], dp[i-1][j])
            else : 
                dp[i][j] = dp[i-1][j]
    return dp[N][T]

if __name__ == "__main__" : 
    N, T = map(int, input().split())
    tLi = [0] * N        # time list
    sLi = [0] * N        # score list
    for i in range(N) : 
        K, S = map(int, input().split())
        tLi[i] = K
        sLi[i] = S
    
    print(chk(T, tLi, sLi, N))